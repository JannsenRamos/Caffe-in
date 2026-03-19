#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install transformers torch scikit-learn scipy faiss-cpu')


# In[3]:


import torch
import transformers
import sklearn
import scipy
import faiss

print("Torch:", torch.__version__)
print("Transformers:", transformers.__version__)
print("scikit-learn:", sklearn.__version__)
print("scipy:", scipy.__version__)
print("FAISS:", faiss.__version__)


# In[6]:


import torch
from transformers import DistilBertTokenizer, DistilBertModel

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertModel.from_pretrained("distilbert-base-uncased")
print(torch.cuda.is_available())
print("Models loaded successfully")


# In[7]:


import torch
from transformers import DistilBertTokenizer, DistilBertModel

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertModel.from_pretrained("distilbert-base-uncased")


# In[12]:


import torch
import numpy as np
import pandas as pd
from transformers import DistilBertTokenizer, DistilBertModel
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_distances

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModel.from_pretrained("distilbert-base-uncased")

    # Put the model in evaluation mode for inference
    model.eval()

    return tokenizer, model

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output.last_hidden_state
    # Expand mask to match embeddings
    mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    # Apply mask and compute mean
    sum_embeddings = (token_embeddings * mask_expanded).sum(1)
    sum_mask = mask_expanded.sum(1)
    mean_pooled = sum_embeddings / sum_mask.clamp(min=1e-9)  # avoid division by zero

    return mean_pooled

def embed_reviews(df: pd.DataFrame, batch_size: int = 32) -> np.ndarray:
    tokenizer, model = load_model()
    review_list = df["review"].tolist()
    sentence_embeddings = []

    for i in range(0, len(review_list), batch_size):
        batch_review = review_list[i:i+batch_size]

        encoded = tokenizer(
        batch_review,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="pt"
        )

        with torch.no_grad():
            model_output = model(**encoded)

        batch_embeddings = mean_pooling(model_output, encoded["attention_mask"])
        sentence_embeddings.append(batch_embeddings)
    sentence_embeddings = torch.cat(sentence_embeddings, dim=0)

    sentence_embeddings = sentence_embeddings.numpy()
    return sentence_embeddings

def compute_product_embeddings(df: pd.DataFrame, embeddings: np.ndarray) -> tuple:
    grouped_coffee = df.groupby("coffee_name")

    coffee_names = []
    coffee_centroids = []

    for coffee, group in grouped_coffee:
        indices = group.index.tolist()
        coffee_embeds = embeddings[indices]              
        mean_embed = coffee_embeds.mean(axis=0)          

        coffee_names.append(coffee)
        coffee_centroids.append(mean_embed)

    coffee_centroids = np.vstack(coffee_centroids)      

    return coffee_centroids, coffee_names


def compute_variance_scores(df: pd.DataFrame, embeddings: np.ndarray, product_embeddings: np.ndarray) -> np.ndarray:
    variance_scores = []
    grouped_coffee = df.groupby("coffee_name").groups
    coffee_to_centroid = {
        coffee: product_embeddings[i]
        for i, coffee in enumerate(grouped_coffee.keys())
    }
    for coffee, indices in grouped_coffee.items():
        review_embeds = embeddings[list(indices)]
        centroid = coffee_to_centroid[coffee].reshape(1, -1)
        distances = cosine_distances(review_embeds, centroid).flatten()
        variance = np.mean(distances)
        variance_scores.append(variance)

    return np.array(variance_scores)


# In[13]:


def build_embedding_pipeline(df: pd.DataFrame):
    embeddings = embed_reviews(df)
    product_embeddings, coffee_names = compute_product_embeddings(df, embeddings)
    variance_scores = compute_variance_scores(df, embeddings, product_embeddings)

    np.save("embeddings.npy", embeddings)
    np.save("product_embeddings.npy", product_embeddings)
    np.save("variance_scores.npy", variance_scores)
    np.save("coffee_names.npy", coffee_names)


# In[14]:


df = pd.read_parquet(r"C:\Users\Lenovo\Downloads\anaconda_projects_06b8f467-3fd5-49d3-933a-58539a3f31be_coffee_clean (1).parquet")
build_embedding_pipeline(df)


# In[15]:


embeddings = np.load("embeddings.npy")
product_embeddings = np.load("product_embeddings.npy")
variance_scores = np.load("variance_scores.npy")
coffee_names = np.load("coffee_names.npy", allow_pickle=True)

print(embeddings.shape)
print(product_embeddings.shape)
print(variance_scores.shape)
print(coffee_names.shape)
print(variance_scores.min(), variance_scores.mean(), variance_scores.max())


# In[ ]:




