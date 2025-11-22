"""
Test script for API endpoints
"""

import requests
import json


def test_health_endpoint(base_url='http://localhost:5000'):
    """Test health check endpoint"""
    print(f"\n{'='*60}")
    print("Testing /health endpoint")
    print(f"{'='*60}")
    
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✓ Health check passed")
        else:
            print("✗ Health check failed")
            
    except Exception as e:
        print(f"✗ Error: {e}")


def test_recommend_endpoint(base_url='http://localhost:5000'):
    """Test recommendation endpoint"""
    print(f"\n{'='*60}")
    print("Testing /recommend endpoint")
    print(f"{'='*60}")
    
    test_queries = [
        "I am hiring for Java developers who can also collaborate effectively with my business teams.",
        "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript.",
        "Need assessment for analyst role with cognitive and personality tests"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\nTest {i}: {query}")
        print("-" * 60)
        
        try:
            response = requests.post(
                f"{base_url}/recommend",
                json={"query": query},
                headers={"Content-Type": "application/json"}
            )
            
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"Total recommendations: {data['total_recommendations']}")
                print(f"\nTop 5 recommendations:")
                
                for j, rec in enumerate(data['recommendations'][:5], 1):
                    print(f"{j}. {rec['assessment_name']}")
                    print(f"   Type: {rec['test_type']} | Score: {rec['relevance_score']:.3f}")
                    print(f"   URL: {rec['url']}")
                
                print("✓ Test passed")
            else:
                print(f"Response: {response.json()}")
                print("✗ Test failed")
                
        except Exception as e:
            print(f"✗ Error: {e}")


def test_api_info_endpoint(base_url='http://localhost:5000'):
    """Test API info endpoint"""
    print(f"\n{'='*60}")
    print("Testing /api/info endpoint")
    print(f"{'='*60}")
    
    try:
        response = requests.get(f"{base_url}/api/info")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✓ API info test passed")
        else:
            print("✗ API info test failed")
            
    except Exception as e:
        print(f"✗ Error: {e}")


def main():
    """Run all tests"""
    print(f"\n{'#'*60}")
    print("API Testing Suite")
    print(f"{'#'*60}")
    
    base_url = input("\nEnter API base URL (default: http://localhost:5000): ").strip()
    if not base_url:
        base_url = "http://localhost:5000"
    
    # Run tests
    test_health_endpoint(base_url)
    test_api_info_endpoint(base_url)
    test_recommend_endpoint(base_url)
    
    print(f"\n{'#'*60}")
    print("Testing Complete")
    print(f"{'#'*60}\n")


if __name__ == "__main__":
    main()
