import requests

response = requests.post("http://127.0.0.1:8000/search", json={
    "query": "bright citrus floral",
    "top_k": 5,
    "roast_level": "Light"
})

print(response.json())