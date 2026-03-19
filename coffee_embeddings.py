import numpy as np
import pandas as pd
import torch
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


def build_embedding_pipeline(df: pd.DataFrame):
    embeddings = embed_reviews(df)
    product_embeddings, coffee_names = compute_product_embeddings(df, embeddings)
    variance_scores = compute_variance_scores(df, embeddings, product_embeddings)

    np.save("embeddings.npy", embeddings)
    np.save("product_embeddings.npy", product_embeddings)
    np.save("variance_scores.npy", variance_scores)
    np.save("coffee_names.npy", coffee_names)

