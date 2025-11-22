"""Quick API test"""
import requests
import json

# Test health
print("Testing /health...")
r = requests.get("http://localhost:5000/health")
print(f"Status: {r.status_code}")
print(f"Response: {json.dumps(r.json(), indent=2)}\n")

# Test recommend
print("Testing /recommend...")
r = requests.post(
    "http://localhost:5000/recommend",
    json={"query": "Java developer with collaboration skills"}
)
print(f"Status: {r.status_code}")
data = r.json()

if "recommended_assessments" in data:
    print(f"Found {len(data['recommended_assessments'])} assessments")
    print(f"\nFirst assessment:")
    print(json.dumps(data['recommended_assessments'][0], indent=2))
    
    # Show test types
    types = [a['test_type'][0] for a in data['recommended_assessments'][:10]]
    print(f"\nTest types in results: {set(types)}")
