# ☕ Caffe-In
### Semantic Coffee Recommendations Powered by Flavor Language

> *Most recommendation systems tell you what to try. Caffe-In tells you why — and how risky the pick is.*

---

## The Problem

Everyone has a staple coffee — the one that gets you through Monday morning. But at some point you want to branch out. You go café hopping, you see an unfamiliar origin on the menu, and you wonder: *will I actually like this?*

Generic recommendation systems answer that question with a star rating or a vague "customers also bought." They tell you what is popular, not what matches your palate. And they never tell you why.

Caffe-In is different. You describe your ideal cup in plain language — *"bright citrus floral light roast"* or *"dark chocolate nutty bold espresso"* — and the system finds coffees that are semantically similar to your description, ranked by how closely their actual tasting notes match what you want.

More importantly, it tells you **how confident to be in that recommendation** through a risk score — so you know whether you're picking a safe, consistent coffee or an adventurous, unpredictable one.

---

## The Core Innovation

Most NLP recommendation systems stop at similarity. Caffe-In adds a second dimension borrowed from portfolio theory: **intra-product embedding variance**.

Each coffee has multiple professional tasting notes. Caffe-In embeds every review independently using DistilBERT, then computes how spread out those embeddings are around the product's centroid. A tight cluster means reviewers consistently agree on the flavor profile — low risk, predictable experience. A scattered cluster means reviewers fundamentally disagree — high risk, adventurous pick.

This turns a semantic search engine into a **risk-return recommendation system**:

| Risk Level | Variance Range | What It Means |
|---|---|---|
| 🟢 Low | < 0.030 | Consistent, predictable flavor |
| 🟡 Medium | 0.030 – 0.060 | Moderately consistent |
| 🔴 High | > 0.060 | Adventurous, variable experience |

---

## How It Works

```
Raw scraped data + Kaggle CoffeeReview dataset
            ↓
    Data pipeline (ingestion, merging, cleaning)
            ↓
    DistilBERT embeddings (768-dim per review)
            ↓
    Per-product centroid + variance score
            ↓
    FAISS index for fast similarity search
            ↓
    FastAPI backend + Streamlit demo UI
```

**Dataset:** 9,358 professional tasting notes across 2,016 unique coffees, minimum 3 reviews per product. Sourced from CoffeeReview.com scrape and Kaggle CoffeeReview dataset.

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data pipeline | Python, Pandas, NumPy |
| NLP & Embeddings | HuggingFace Transformers, DistilBERT |
| Vector search | FAISS (`faiss-cpu`) |
| Backend API | FastAPI, Uvicorn |
| Demo UI | Streamlit, Plotly |
| Serialization | Parquet, NumPy `.npy` |

---

## Project Structure

```
caffe-in/
│
├── coffee_pipeline.py          # data ingestion, merging, cleaning
├── coffee_embedding.py         # DistilBERT embeddings, centroids, variance scores
├── coffee_search.py            # FAISS index, semantic search
├── app.py               # FastAPI REST API
├── app_ui.py              # Streamlit demo UI
│
├── dataset/
│   ├── coffee_clean.parquet
│   ├── embeddings.npy
│   ├── product_embeddings.npy
│   ├── variance_scores.npy
│   └── coffee_names.npy
│
└── eda/
    └── eda.ipynb        # exploratory data analysis
```

---

## Getting Started

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the data pipeline**
```bash
python pipeline.py
```

**3. Generate embeddings** *(runs on CPU, ~15–30 minutes)*
```bash
python embedding.py
```

**4. Launch the demo**
```bash
streamlit run demo.py
```

**5. Or run the API**
```bash
uvicorn app:app --reload
```

API endpoint: `POST http://127.0.0.1:8000/search`
```json
{
    "query": "bright citrus floral light roast",
    "top_k": 5,
    "roast_level": "Light"
}
```

---

## Example Results

Query: *"dark chocolate nutty bold espresso"*

```
winter day espresso blend     similarity: 0.885  risk: 🔴 High
firebird espresso             similarity: 0.872  risk: 🔴 High
kaori espresso blend          similarity: 0.870  risk: 🟡 Medium
secret lovers blend           similarity: 0.870  risk: 🟡 Medium
syunmei espresso blend        similarity: 0.870  risk: 🟡 Medium
```

---

## Limitations & Future Work

- **Variance range is narrow (0.008–0.085)** because all reviews come from a single professional source (CoffeeReview.com). Incorporating user-generated reviews would widen the variance distribution and improve risk score resolution.
- **No user feedback loop** — the system has no mechanism to learn from user preferences over time. A future version could incorporate implicit feedback (clicks, saves) to personalize recommendations.
- **Roast level filter is post-retrieval** — a production system would benefit from hybrid search combining dense semantic retrieval with structured metadata filtering at the index level.
- **API is not authenticated** — production deployment would require rate limiting and API key management.

---

## About

Built as part of a data science portfolio targeting fintech and ML engineering roles. Caffe-In demonstrates end-to-end NLP system design — from raw data ingestion through embedding, indexing, serving, and explainable recommendation output.

---

*Made with ☕ and too many tasting notes.*
