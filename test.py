import requests

response = requests.post(
    "http://127.0.0.1:8000/search",
    json={
        "query": "dark chocolate nutty bold",
        "top_k": 5,
        "roast_level": "Medium-Dark"
    }
)

print(response.json())