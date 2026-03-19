import numpy as np
import pandas as pd
from coffee_embeddings import load_model
from search import build_faiss_index, search

# load saved artifacts
product_embeddings = np.load("dataset/product_embeddings.npy")
variance_scores = np.load("dataset/variance_scores.npy")
coffee_names = np.load("dataset/coffee_names.npy", allow_pickle=True)

# build index
index = build_faiss_index(product_embeddings)

# load model
tokenizer, model = load_model()

# run a test query
results = search(
    query="smooth caramel sweet medium roast",
    tokenizer=tokenizer,
    model=model,
    index=index,
    coffee_names=coffee_names,
    variance_scores=variance_scores,
    top_k=5
)

for r in results:
    print({
        "name": str(r["name"]),
        "similarity": round(float(r["score"]), 4),
        "variance": round(float(r["variance"]), 4)
    })