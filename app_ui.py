import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from coffee_embeddings import load_model
from search import build_faiss_index, search

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Caffe-In",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --espresso:   #1C0A00;
    --roast:      #3B1F0E;
    --caramel:    #C68642;
    --cream:      #F5ECD7;
    --milk:       #FDF8F0;
    --low:        #4A7C59;
    --mid:        #C68642;
    --high:       #A63D2F;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--milk);
    color: var(--espresso);
}

h1, h2, h3 { font-family: 'Playfair Display', serif; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background-color: var(--roast);
    border-right: 3px solid var(--caramel);
}
section[data-testid="stSidebar"] * {
    color: var(--cream) !important;
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label,
section[data-testid="stSidebar"] .stTextInput label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.8rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--caramel) !important;
}

/* ── Header ── */
.caffe-header {
    padding: 2rem 0 1rem;
    border-bottom: 2px solid var(--caramel);
    margin-bottom: 2rem;
}
.caffe-header h1 {
    font-size: 3.2rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--espresso);
    margin: 0;
}
.caffe-header h1 span { color: var(--caramel); }
.caffe-header p {
    font-size: 1rem;
    color: #6B4F3A;
    margin-top: 0.4rem;
    font-weight: 300;
    font-style: italic;
}

/* ── Result card ── */
.coffee-card {
    background: #fff;
    border: 1px solid #E8D9C5;
    border-left: 5px solid var(--caramel);
    border-radius: 6px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(28,10,0,0.06);
    transition: box-shadow 0.2s ease;
}
.coffee-card:hover { box-shadow: 0 4px 16px rgba(28,10,0,0.12); }
.coffee-card h3 {
    font-size: 1.25rem;
    margin: 0 0 0.2rem;
    color: var(--espresso);
    text-transform: capitalize;
}
.roast-tag {
    display: inline-block;
    background: var(--cream);
    border: 1px solid var(--caramel);
    color: var(--roast);
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 2px 10px;
    border-radius: 20px;
    margin-bottom: 0.8rem;
    font-weight: 500;
}
.review-snippet {
    font-size: 0.9rem;
    color: #5C4033;
    font-style: italic;
    line-height: 1.6;
    margin: 0.6rem 0;
    border-left: 3px solid var(--cream);
    padding-left: 0.8rem;
}
.risk-badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.05em;
    margin-top: 0.4rem;
}
.risk-low  { background: #E8F5ED; color: var(--low);  border: 1px solid var(--low); }
.risk-mid  { background: #FEF3E2; color: var(--mid);  border: 1px solid var(--mid); }
.risk-high { background: #FDECEA; color: var(--high); border: 1px solid var(--high); }

/* ── Metrics row ── */
.metric-row {
    display: flex;
    gap: 1rem;
    margin-top: 0.8rem;
}
.metric-box {
    background: var(--cream);
    border-radius: 6px;
    padding: 0.5rem 1rem;
    text-align: center;
    flex: 1;
}
.metric-box .label {
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #8B6348;
}
.metric-box .value {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--espresso);
    font-family: 'Playfair Display', serif;
}

/* ── Legend ── */
.legend-box {
    background: var(--cream);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-top: 1.5rem;
    font-size: 0.82rem;
    line-height: 1.8;
    color: var(--roast);
}
.legend-box strong { color: var(--espresso); }

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: #A08060;
}
.empty-state .icon { font-size: 3rem; margin-bottom: 1rem; }
.empty-state p { font-style: italic; font-size: 1rem; }

/* ── Section title ── */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    color: var(--espresso);
    border-bottom: 1px solid #E8D9C5;
    padding-bottom: 0.4rem;
    margin: 2rem 0 1rem;
    letter-spacing: 0.02em;
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ────────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="Warming up the grinder...")
def load_resources():
    tokenizer, model = load_model()
    product_embeddings = np.load("dataset/product_embeddings.npy")
    index = build_faiss_index(product_embeddings)
    coffee_names   = np.load("dataset/coffee_names.npy",   allow_pickle=True)
    variance_scores = np.load("dataset/variance_scores.npy")
    df = pd.read_parquet("dataset/coffee_clean.parquet")
    return tokenizer, model, index, coffee_names, variance_scores, df


def get_risk_label(variance: float):
    if variance < 0.030:
        return "Low Risk",  "low",  "🟢 Consistent & predictable"
    elif variance < 0.060:
        return "Medium Risk", "mid", "🟡 Moderately consistent"
    else:
        return "High Risk", "high", "🔴 Adventurous & variable"


def get_top_review(df: pd.DataFrame, coffee_name: str) -> str:
    rows = df[df["coffee_name"] == coffee_name].sort_values("score", ascending=False)
    if len(rows) == 0:
        return ""
    review = rows.iloc[0]["review"]
    # truncate to ~200 chars for card display
    return review[:220] + "..." if len(review) > 220 else review


# ── Load once ──────────────────────────────────────────────────────────────────
tokenizer, model, index, coffee_names, variance_scores, df = load_resources()

ROAST_OPTIONS = ["All", "Light", "Medium-Light", "Medium", "Medium-Dark", "Dark", "Very Dark"]

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ☕ Caffe-In")
    st.markdown("---")

    roast_level = st.selectbox("Roast Level", ROAST_OPTIONS)
    top_k       = st.slider("Results to show", min_value=1, max_value=15, value=5)

    st.markdown("---")
    st.markdown("""
<div class='legend-box'>
<strong>Risk Score Guide</strong><br>
🟢 <strong>Low</strong> — reviewers consistently agree on flavors<br>
🟡 <strong>Medium</strong> — moderate variation between reviews<br>
🔴 <strong>High</strong> — adventurous; flavors are unpredictable<br><br>
<em>Think of it like a portfolio: low variance = safe bet, high variance = bold pick.</em>
</div>
""", unsafe_allow_html=True)


# ── Main area ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class='caffe-header'>
  <h1>Caffe<span>-In</span></h1>
  <p>Semantic coffee recommendations powered by flavor language — not stars.</p>
</div>
""", unsafe_allow_html=True)

col_input, col_btn = st.columns([5, 1])
with col_input:
    query = st.text_input(
        label="query",
        placeholder="Describe your ideal cup — e.g. bright citrus floral light roast...",
        label_visibility="collapsed"
    )
with col_btn:
    search_clicked = st.button("Search ☕", use_container_width=True)


# ── Search & results ───────────────────────────────────────────────────────────
if search_clicked and query.strip():
    with st.spinner("Brewing your recommendations..."):
        fetch_k = top_k * 3 if roast_level != "All" else top_k

        raw_results = search(
            query=query,
            tokenizer=tokenizer,
            model=model,
            index=index,
            coffee_names=coffee_names,
            variance_scores=variance_scores,
            top_k=fetch_k,
        )

        # attach metadata
        enriched = []
        for r in raw_results:
            rows = df[df["coffee_name"] == r["name"]]
            if len(rows) == 0:
                continue
            roast = rows.iloc[0]["roast_level"]
            if roast_level != "All" and roast.lower() != roast_level.lower():
                continue
            label, css_class, description = get_risk_label(r["variance"])
            enriched.append({
                **r,
                "roast_level":   roast,
                "risk_label":    label,
                "risk_class":    css_class,
                "risk_desc":     description,
                "top_review":    get_top_review(df, r["name"]),
            })
            if len(enriched) == top_k:
                break

    if not enriched:
        st.markdown("""
<div class='empty-state'>
  <div class='icon'>☕</div>
  <p>No coffees matched your filters. Try a different roast level or broaden your query.</p>
</div>
""", unsafe_allow_html=True)
    else:
        # ── Result cards ──
        st.markdown(f"<div class='section-title'>Top {len(enriched)} Matches</div>", unsafe_allow_html=True)

        for r in enriched:
            st.markdown(f"""
<div class='coffee-card'>
  <h3>{r['name'].title()}</h3>
  <span class='roast-tag'>{r['roast_level']} Roast</span>
  <div class='review-snippet'>"{r['top_review']}"</div>
  <div class='metric-row'>
    <div class='metric-box'>
      <div class='label'>Similarity</div>
      <div class='value'>{r['score']:.3f}</div>
    </div>
    <div class='metric-box'>
      <div class='label'>Variance</div>
      <div class='value'>{r['variance']:.4f}</div>
    </div>
  </div>
  <span class='risk-badge risk-{r["risk_class"]}'>{r['risk_label']} — {r['risk_desc']}</span>
</div>
""", unsafe_allow_html=True)

        # ── Charts ──
        chart_df = pd.DataFrame(enriched)
        chart_df["name_display"] = chart_df["name"].str.title().str[:28]

        st.markdown("<div class='section-title'>Visual Analysis</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            fig_bar = px.bar(
                chart_df,
                x="score",
                y="name_display",
                orientation="h",
                title="Similarity Scores",
                color="score",
                color_continuous_scale=["#E8D9C5", "#C68642", "#3B1F0E"],
                labels={"score": "Similarity", "name_display": ""},
            )
            fig_bar.update_layout(
                plot_bgcolor="#FDF8F0",
                paper_bgcolor="#FDF8F0",
                font_family="DM Sans",
                coloraxis_showscale=False,
                margin=dict(l=0, r=10, t=40, b=10),
                title_font_family="Playfair Display",
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            fig_scatter = px.scatter(
                chart_df,
                x="score",
                y="variance",
                text="name_display",
                title="Similarity vs Risk",
                color="variance",
                color_continuous_scale=["#4A7C59", "#C68642", "#A63D2F"],
                labels={"score": "Similarity", "variance": "Risk (Variance)"},
                size=[12] * len(chart_df),
            )
            fig_scatter.update_traces(textposition="top center", textfont_size=9)
            fig_scatter.update_layout(
                plot_bgcolor="#FDF8F0",
                paper_bgcolor="#FDF8F0",
                font_family="DM Sans",
                coloraxis_showscale=False,
                margin=dict(l=0, r=10, t=40, b=10),
                title_font_family="Playfair Display",
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

elif search_clicked and not query.strip():
    st.warning("Please enter a flavor description to search.")

else:
    st.markdown("""
<div class='empty-state'>
  <div class='icon'>☕</div>
  <p>Describe your ideal cup above and hit Search to discover your next favorite coffee.</p>
</div>
""", unsafe_allow_html=True)