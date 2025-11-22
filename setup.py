"""
Setup script to initialize the SHL recommendation system
Runs scraper, generates embeddings, and prepares the system
"""

import sys
import os
import logging

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scraper import SHLScraper
from src.embeddings import EmbeddingManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup():
    """Run full setup"""
    print(f"\n{'='*80}")
    print("SHL Assessment Recommendation System - Setup")
    print(f"{'='*80}\n")
    
    # Step 1: Scrape catalog
    print("\n[1/3] Scraping SHL catalog...")
    print("-" * 80)
    
    scraper = SHLScraper()
    assessments = scraper.scrape_catalog()
    scraper.save_to_json()
    
    print(f"✓ Scraped {len(assessments)} assessments")
    
    # Step 2: Generate embeddings
    print("\n[2/3] Generating embeddings...")
    print("-" * 80)
    
    manager = EmbeddingManager()
    manager.load_assessments()
    manager.generate_embeddings()
    manager.build_faiss_index()
    manager.save_embeddings()
    
    print(f"✓ Generated embeddings for {len(manager.assessments)} assessments")
    
    # Step 3: Test system
    print("\n[3/3] Testing system...")
    print("-" * 80)
    
    test_query = "Java developer with communication skills"
    results = manager.search_with_diversity(test_query, k=5)
    
    print(f"Test query: {test_query}")
    print(f"Found {len(results)} recommendations")
    
    for i, (assessment, score) in enumerate(results[:3], 1):
        print(f"  {i}. {assessment['assessment_name']} (Score: {score:.3f})")
    
    print(f"\n{'='*80}")
    print("Setup Complete!")
    print(f"{'='*80}")
    print("\nNext steps:")
    print("1. Set your Google Gemini API key in .env file")
    print("2. Run the API: python api/app.py")
    print("3. Open http://localhost:5000 in your browser")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    setup()
