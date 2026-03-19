from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from embeddings import load_model
from search import build_faiss_index, search

app = FastAPI()

# load artifacts and model once at startup
tokenizer, model = load_model()
index = build_faiss_index(np.load("dataset/product_embeddings.npy"))
coffee_names = np.load("dataset/coffee_names.npy")
variance_scores = np.load("dataset/variance_scores.npy")
df = pd.read_csv("dataset/coffee_reviewsV2.csv")

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    roast_level: str = None

@app.post("/search")
def search_endpoint(request: SearchRequest):

    fetch_k = request.top_k * 3 if request.roast_level else request.top_k

    results = search(
        query=request.query,
        tokenizer=tokenizer,
        model=model,
        index=index,
        coffee_names=coffee_names,
        variance_scores=variance_scores,
        top_k=fetch_k,
    )
    if request.roast_level:
        filtered = []
        for r in results:
            roast = df.loc[df["coffee_name"] == r["name"], "roast_level"].values
            if len(roast) > 0 and roast[0].lower() == request.roast_level.lower():
                r["roast_level"] = roast[0]
                filtered.append(r)
        results = filtered

    else:
        for r in results:
            roast = df.loc[df["coffee_name"] == r["name"], "roast_level"].values
            if len(roast) > 0:
                r["roast_level"] = roast[0]

    return {"query": request.query, "results": results}