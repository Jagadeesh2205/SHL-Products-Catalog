"""
Vercel-optimized Flask API for SHL Assessment Recommendation System
Lightweight version with minimal memory footprint
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
import json
import logging

# Configure minimal logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Global variables for lazy loading
_assessments = None
_recommender = None


def load_assessments():
    """Load assessments from JSON file (lazy loading)"""
    global _assessments
    if _assessments is None:
        try:
            data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'scraped_data.json')
            with open(data_path, 'r', encoding='utf-8') as f:
                _assessments = json.load(f)
            logger.info(f"Loaded {len(_assessments)} assessments")
        except Exception as e:
            logger.error(f"Error loading assessments: {e}")
            _assessments = []
    return _assessments


def get_recommender():
    """Get recommender instance (lazy loading)"""
    global _recommender
    if _recommender is None:
        try:
            from src.recommender import RAGRecommender
            _recommender = RAGRecommender()
        except Exception as e:
            logger.error(f"Error initializing recommender: {e}")
            # Fallback to simple keyword matching
            _recommender = SimpleRecommender()
    return _recommender


class SimpleRecommender:
    """Lightweight fallback recommender using keyword matching"""
    
    def __init__(self):
        self.assessments = load_assessments()
    
    def recommend(self, query: str, k: int = 10) -> list:
        """Simple keyword-based recommendations"""
        query_lower = query.lower()
        words = set(query_lower.split())
        
        # Score each assessment
        scored = []
        for assessment in self.assessments:
            score = 0
            text = f"{assessment['assessment_name']} {assessment.get('description', '')} {assessment.get('category', '')}".lower()
            
            # Count word matches
            for word in words:
                if len(word) > 3 and word in text:
                    score += 1
            
            if score > 0:
                assessment_copy = assessment.copy()
                assessment_copy['relevance_score'] = score
                scored.append(assessment_copy)
        
        # Sort by score and return top k
        scored.sort(key=lambda x: x['relevance_score'], reverse=True)
        return scored[:k]


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Assessment recommendation endpoint
    Optimized for Vercel serverless functions
    """
    try:
        # Validate request
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
        
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query or len(query) < 3:
            return jsonify({'error': 'Invalid query'}), 400
        
        # Limit query length to prevent memory issues
        query = query[:2000]
        
        # Get number of recommendations (5-10)
        k = min(10, max(5, data.get('k', 10)))
        
        # Get recommender and generate recommendations
        recommender = get_recommender()
        recommendations = recommender.recommend(query, k=k)
        
        # Format response (lightweight)
        formatted = []
        for rec in recommendations[:k]:
            formatted.append({
                'url': rec.get('url', ''),
                'name': rec.get('assessment_name', ''),
                'adaptive_support': rec.get('adaptive_support', 'No'),
                'description': rec.get('description', '')[:200],  # Limit description length
                'duration': rec.get('duration', 0),
                'remote_support': rec.get('remote_support', 'Yes'),
                'test_type': [rec.get('test_type_full', rec.get('category', 'Other'))]
            })
        
        return jsonify({'recommended_assessments': formatted}), 200
        
    except Exception as e:
        logger.error(f"Error in recommend: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/info', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        'name': 'SHL Assessment Recommendation API',
        'version': '1.0.0',
        'status': 'operational'
    }), 200


# Vercel serverless function handler
def handler(request):
    """Vercel serverless function handler"""
    with app.request_context(request.environ):
        return app.full_dispatch_request()
