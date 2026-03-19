#!/usr/bin/env python
# coding: utf-8

# In[1]:


import faiss
from sklearn.preprocessing import normalize
from coffee_embeddings import mean_pooling


# In[ ]:


def build_faiss_index(product_embeddings: np.ndarray) -> faiss.Index:
    product_embeddings_normalized = normalize(product_embeddings, norm="l2")

    dimension = product_embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(product_embeddings_normalized)

    return index

def search(query: str, tokenizer, model, index: faiss.Index, 
           coffee_names: np.ndarray, variance_scores: np.ndarray, 
           top_k: int = 5) -> list:

    encoded = tokenizer(query, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**encoded)

    query_embedding = mean_pooling(outputs, encoded["attention_mask"])

    query_vector = normalize(query_embedding, norm="l2")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "name": coffee_names[idx],
            "variance": variance_scores[idx],
            "score": distances[0][i]
        })

    return results


# In[2]:


import os
print(os.getcwd())


# In[ ]:




