from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from embedding import load_model
from search import build_faiss_index, search

app = FastAPI()

# load artifacts and model once at startup
# your code here

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    roast_level: str = None

@app.post("/search")
def search_endpoint(request: SearchRequest):
    pass