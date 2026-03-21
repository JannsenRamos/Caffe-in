import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from coffee_embeddings import load_model
from search import build_faiss_index, search

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Caffe-In | Your Coffee Sommelier",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS (Design System from Stitch export) ──────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400;1,6..72,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── Design Tokens ── */
:root {
    --primary:                   #6c2f00;
    --secondary:                 #934b00;
    --tertiary:                  #174a2b;
    --error:                     #ba1a1a;
    --surface:                   #fef9f1;
    --surface-container:         #f2ede5;
    --surface-container-low:     #f8f3eb;
    --surface-container-high:    #ece8e0;
    --surface-container-highest: #e7e2da;
    --on-surface:                #1d1c17;
    --on-surface-variant:        #54433a;
    --outline-variant:           #dac2b6;
    --outline:                   #877369;
    --primary-fixed:             #ffdbc9;
    --secondary-container:       #fea054;
}

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: var(--surface) !important;
    color: var(--on-surface) !important;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 3rem !important;
    max-width: 1200px;
}

/* ── Sidebar (collapsed by default; keep styled if user opens) ── */
section[data-testid="stSidebar"] {
    background-color: var(--surface-container-low);
    border-right: 1px solid var(--outline-variant);
}

/* ── Typography helpers ── */
.font-headline { font-family: 'Newsreader', serif !important; }
.font-mono     { font-family: 'IBM Plex Mono', monospace !important; }

/* ── Top Nav Bar ── */
.ci-nav {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(254, 249, 241, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--outline-variant);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.1rem 2.5rem;
    margin: -1rem -1rem 0 -1rem;
}
.ci-nav .ci-logo {
    font-family: 'Newsreader', serif;
    font-style: italic;
    font-size: 1.6rem;
    color: var(--on-surface);
    letter-spacing: -0.02em;
}
.ci-nav .ci-nav-links {
    display: flex;
    gap: 2.5rem;
}
.ci-nav .ci-nav-links a {
    font-size: 0.88rem;
    font-weight: 500;
    color: rgba(29,28,23,0.55);
    text-decoration: none;
    transition: color 0.2s;
}
.ci-nav .ci-nav-links a:hover { color: var(--primary); }

/* ── Hero Section ── */
.ci-hero {
    text-align: center;
    padding: 4.5rem 1rem 2.5rem;
    position: relative;
    overflow: hidden;
}
.ci-hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -80px;
    width: 340px; height: 340px;
    background: radial-gradient(circle, #ffb68c44 0%, transparent 70%);
    pointer-events: none;
}
.ci-hero::after {
    content: '';
    position: absolute;
    bottom: -40px; left: -60px;
    width: 220px; height: 220px;
    background: radial-gradient(circle, #9dd3aa22 0%, transparent 70%);
    pointer-events: none;
}
.ci-hero h1 {
    font-family: 'Newsreader', serif !important;
    font-style: italic;
    font-size: clamp(2.6rem, 6vw, 5rem);
    font-weight: 400;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: var(--on-surface);
    margin: 0 0 1rem;
}
.ci-hero p {
    font-size: 1.05rem;
    font-weight: 300;
    color: var(--on-surface-variant);
    max-width: 540px;
    margin: 0 auto 2.4rem;
    line-height: 1.7;
}

/* ── Search Bar ── */
.ci-search-wrap {
    max-width: 640px;
    margin: 0 auto;
    position: relative;
}

/* Override Streamlit form / text input to look like pill input */
.ci-search-wrap .stForm {
    border: none !important;
    padding: 0 !important;
    background: transparent !important;
}
.ci-search-wrap [data-testid="stTextInput"] input {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1rem !important;
    background: #fff !important;
    border: 1.5px solid var(--outline-variant) !important;
    border-radius: 9999px !important;
    padding: 0.9rem 1.8rem !important;
    color: var(--on-surface) !important;
    box-shadow: 0 8px 28px rgba(29,28,23,0.07) !important;
    transition: border-color 0.25s, box-shadow 0.25s !important;
}
.ci-search-wrap [data-testid="stTextInput"] input:focus {
    border-color: var(--secondary) !important;
    box-shadow: 0 8px 28px rgba(147,75,0,0.12) !important;
    outline: none !important;
}
.ci-search-wrap [data-testid="stTextInput"] label { display: none !important; }

/* Submit button */
.ci-search-wrap [data-testid="stFormSubmitButton"] button {
    background: var(--secondary) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 9999px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.75rem 2rem !important;
    transition: background 0.2s, transform 0.15s !important;
    cursor: pointer !important;
    width: 100% !important;
}
.ci-search-wrap [data-testid="stFormSubmitButton"] button:hover {
    background: var(--primary) !important;
    transform: translateY(-1px) !important;
}

/* ── Roast Filter Pills (radio → pills via CSS) ── */
.ci-roast-filter { margin: 1.8rem auto; max-width: 640px; text-align: center; }
.ci-roast-filter p { display: none; }   /* hide default radio label */
.ci-roast-filter [role="radiogroup"] {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: center !important;
    gap: 0.5rem !important;
}
.ci-roast-filter [role="radiogroup"] label {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0 !important;
    cursor: pointer !important;
}
.ci-roast-filter [role="radiogroup"] label span:last-child {
    padding: 0.35rem 1.1rem !important;
    border-radius: 9999px !important;
    border: 1.5px solid var(--outline-variant) !important;
    background: transparent !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    color: var(--on-surface-variant) !important;
    transition: all 0.2s !important;
}
.ci-roast-filter [role="radiogroup"] label:hover span:last-child {
    border-color: var(--secondary) !important;
    background: rgba(147,75,0,0.04) !important;
    color: var(--secondary) !important;
}
/* Selected pill */
.ci-roast-filter [role="radiogroup"] [aria-checked="true"] + div span:last-child,
.ci-roast-filter [data-baseweb="radio"] input:checked ~ div span:last-child {
    background: var(--primary) !important;
    border-color: var(--primary) !important;
    color: #fff !important;
}
/* Hide actual radio circle */
.ci-roast-filter [role="radiogroup"] label span:first-child { display: none !important; }
.ci-roast-filter [data-baseweb="radio"] > div:first-child { display: none !important; }

/* ── Section label (mono uppercase) ── */
.ci-section-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--on-surface-variant);
    opacity: 0.7;
    margin-bottom: 1rem;
}

/* ── Result Cards ── */
.ci-card {
    background: #fff;
    border-radius: 1rem;
    padding: 2rem;
    border: 1px solid var(--outline-variant);
    transition: box-shadow 0.35s, border-color 0.35s;
    height: 100%;
    box-sizing: border-box;
}
.ci-card:hover {
    box-shadow: 0 12px 32px rgba(29,28,23,0.08);
    border-color: rgba(147,75,0,0.25);
}
.ci-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1.2rem;
}
.ci-card h3 {
    font-family: 'Newsreader', serif !important;
    font-size: 1.6rem !important;
    font-weight: 400 !important;
    line-height: 1.2 !important;
    color: var(--on-surface) !important;
    margin: 0 !important;
}
.ci-roast-badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 9999px;
    background: var(--surface-container-high);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--on-surface);
    white-space: nowrap;
    flex-shrink: 0;
    margin-left: 0.8rem;
    margin-top: 0.25rem;
}
.ci-review {
    font-family: 'Newsreader', serif;
    font-style: italic;
    font-size: 1rem;
    color: var(--on-surface-variant);
    line-height: 1.75;
    margin: 0 0 1.4rem;
    border-left: none;
    padding-left: 0;
}

/* ── Match Score Bar ── */
.ci-match-row {
    margin-bottom: 1rem;
}
.ci-match-labels {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.35rem;
}
.ci-match-labels .label {
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--on-surface);
    letter-spacing: 0.02em;
}
.ci-match-labels .pct {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--secondary);
}
.ci-bar-track {
    height: 3px;
    width: 100%;
    background: var(--surface-container-high);
    border-radius: 999px;
    overflow: hidden;
}
.ci-bar-fill {
    height: 100%;
    background: var(--secondary);
    border-radius: 999px;
    transition: width 0.9s cubic-bezier(0.22, 1, 0.36, 1);
}

/* ── Risk Badge ── */
.ci-risk {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.3rem 0.8rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}
.ci-risk .dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    animation: ci-pulse 2.2s ease-in-out infinite;
}
@keyframes ci-pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.55; transform: scale(0.85); }
}
.ci-risk-low  { background: rgba(23,74,43,0.07);  color: #174a2b; }
.ci-risk-low  .dot  { background: #174a2b; }
.ci-risk-mid  { background: rgba(147,75,0,0.08);  color: #934b00; }
.ci-risk-mid  .dot  { background: #934b00; }
.ci-risk-high { background: rgba(186,26,26,0.08); color: #ba1a1a; }
.ci-risk-high .dot  { background: #ba1a1a; }

/* ── Empty State ── */
.ci-empty {
    text-align: center;
    padding: 5rem 2rem 3rem;
}
.ci-empty .big-q {
    font-family: 'Newsreader', serif;
    font-style: italic;
    font-size: 7rem;
    line-height: 1;
    color: var(--outline-variant);
    opacity: 0.5;
    margin-bottom: 1.2rem;
    display: block;
}
.ci-empty h2 {
    font-family: 'Newsreader', serif !important;
    font-size: 2.2rem !important;
    font-weight: 400 !important;
    color: var(--on-surface) !important;
    margin-bottom: 0.7rem !important;
}
.ci-empty p {
    font-size: 1rem;
    color: var(--on-surface-variant);
    max-width: 400px;
    margin: 0 auto 2rem;
    line-height: 1.65;
}
.ci-chips {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.6rem;
    margin-top: 0.5rem;
}
.ci-chip {
    display: inline-block;
    padding: 0.45rem 1.1rem;
    border-radius: 9999px;
    background: var(--surface-container);
    border: 1px solid transparent;
    font-size: 0.84rem;
    color: var(--on-surface);
    transition: background 0.2s, border-color 0.2s;
    cursor: default;
}
.ci-chip:hover {
    background: var(--surface-container-highest);
    border-color: var(--outline-variant);
}

/* ── Section divider ── */
.ci-divider {
    height: 1px;
    background: var(--outline-variant);
    opacity: 0.3;
    margin: 2.5rem 0;
}

/* ── Footer ── */
.ci-footer {
    background: var(--surface-container-low);
    border-top: 1px solid var(--outline-variant);
    padding: 2.5rem 2rem;
    text-align: center;
    margin: 3rem -1rem -3rem;
}
.ci-footer p {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(29,28,23,0.4);
    margin: 0;
}
.ci-footer a {
    color: rgba(29,28,23,0.4);
    text-decoration: none;
    transition: color 0.2s;
    margin: 0 0.8rem;
}
.ci-footer a:hover { color: var(--primary); }

/* ── Visual Analysis section ── */
.ci-charts-header {
    font-family: 'Newsreader', serif;
    font-style: italic;
    font-size: 1.5rem;
    color: var(--on-surface);
    margin: 0 0 0.3rem;
}

/* Top results count badge */
.ci-results-meta {
    display: flex;
    align-items: baseline;
    gap: 0.8rem;
    margin-bottom: 1.8rem;
}
.ci-results-meta .count {
    font-family: 'Newsreader', serif;
    font-style: italic;
    font-size: 2.2rem;
    color: var(--on-surface);
    line-height: 1;
}
.ci-results-meta .label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--on-surface-variant);
}

/* Query echo display */
.ci-query-echo {
    font-family: 'Newsreader', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: var(--on-surface-variant);
    opacity: 0.75;
    margin-bottom: 2rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid rgba(218,194,182,0.4);
}
.ci-query-echo span { opacity: 0.5; font-style: normal; font-family: 'IBM Plex Mono'; font-size: 0.65rem; letter-spacing: 0.15em; text-transform: uppercase; margin-right: 0.8rem; }
</style>
""", unsafe_allow_html=True)


# ── Helpers ────────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="Warming up the grinder…")
def load_resources():
    try:
        tokenizer, model = load_model()
        product_embeddings = np.load("dataset/product_embeddings.npy")
        index = build_faiss_index(product_embeddings)
        coffee_names    = np.load("dataset/coffee_names.npy",   allow_pickle=True)
        variance_scores = np.load("dataset/variance_scores.npy")
        df = pd.read_parquet("dataset/coffee_clean.parquet")
        return tokenizer, model, index, coffee_names, variance_scores, df
    except Exception as e:
        st.error(f"Failed to load resources: {e}")
        st.stop()


def get_risk(variance: float):
    """Return (label, css_class, description) for a given variance."""
    if variance < 0.030:
        return "Low Risk",    "low",  "Consistent, predictable"
    elif variance < 0.060:
        return "Medium Risk", "mid",  "Moderately variable"
    else:
        return "High Risk",   "high", "Adventurous, variable"


def get_top_review(df: pd.DataFrame, coffee_name: str) -> str:
    rows = df[df["coffee_name"] == coffee_name].sort_values("score", ascending=False)
    if len(rows) == 0:
        return ""
    review = rows.iloc[0]["review"]
    return (review[:220] + "…") if len(review) > 220 else review


def run_search(query, roast_level, top_k, tokenizer, model, index,
               coffee_names, variance_scores, df) -> list:
    fetch_k = top_k * 3 if roast_level != "All" else top_k
    try:
        raw = search(
            query=query, tokenizer=tokenizer, model=model,
            index=index, coffee_names=coffee_names,
            variance_scores=variance_scores, top_k=fetch_k,
        )
    except Exception as e:
        st.error(f"Search failed: {e}")
        return []

    enriched = []
    for r in raw:
        rows = df[df["coffee_name"] == r["name"]]
        if len(rows) == 0:
            continue
        roast = rows.iloc[0]["roast_level"]
        if roast_level != "All" and roast.lower() != roast_level.lower():
            continue
        label, css_class, desc = get_risk(r["variance"])
        enriched.append({
            **r,
            "roast_level": roast,
            "risk_label":  label,
            "risk_class":  css_class,
            "risk_desc":   desc,
            "top_review":  get_top_review(df, r["name"]),
        })
        if len(enriched) == top_k:
            break
    return enriched


# ── Load resources ─────────────────────────────────────────────────────────────
tokenizer, model, index, coffee_names, variance_scores, df = load_resources()

ROAST_OPTIONS = ["All", "Light", "Medium-Light", "Medium", "Medium-Dark", "Dark", "Very Dark"]

# ── Session state ──────────────────────────────────────────────────────────────
for key, default in [
    ("results", []),
    ("last_query", ""),
    ("last_roast", "All"),
    ("last_top_k", 5),
    ("searched_once", False),
]:
    if key not in st.session_state:
        st.session_state[key] = default


# ══════════════════════════════════════════════════════════════════════════════
# TOP NAV BAR
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<nav class="ci-nav">
  <div class="ci-logo">Caffe-In</div>
  <div class="ci-nav-links">
    <a href="#">Curations</a>
    <a href="#">Roasters</a>
    <a href="#">Journal</a>
  </div>
</nav>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HERO SECTION
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="ci-hero">
  <h1>Describe your perfect cup.</h1>
  <p>Caffe-In finds coffees that match your flavor language — and tells you how confident to be in the pick.</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEARCH BAR + ROAST FILTER
# ══════════════════════════════════════════════════════════════════════════════
_col_left, _col_search, _col_right = st.columns([1, 4, 1])

with _col_search:
    # Search form (Enter key triggers submit)
    st.markdown('<div class="ci-search-wrap">', unsafe_allow_html=True)
    with st.form("search_form", clear_on_submit=False):
        query_input = st.text_input(
            label="query",
            placeholder="e.g., bright citrus floral light roast…",
            label_visibility="collapsed",
        )
        search_clicked = st.form_submit_button(
            "Find my coffee →",
            use_container_width=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Roast filter pills
    st.markdown('<div class="ci-roast-filter">', unsafe_allow_html=True)
    roast_level = st.radio(
        "Roast level",
        options=ROAST_OPTIONS,
        horizontal=True,
        label_visibility="collapsed",
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Results count slider (compact, below hero)
    top_k = st.slider(
        "Results to show",
        min_value=1, max_value=15, value=5,
        help="How many coffee recommendations to return.",
    )


# ══════════════════════════════════════════════════════════════════════════════
# SEARCH LOGIC
# ══════════════════════════════════════════════════════════════════════════════
should_search = False

if search_clicked and query_input.strip():
    should_search = True
elif search_clicked and not query_input.strip():
    st.warning("Please describe your ideal cup first.")
elif st.session_state.last_query:
    filters_changed = (
        roast_level != st.session_state.last_roast
        or top_k != st.session_state.last_top_k
    )
    if filters_changed:
        query_input = st.session_state.last_query
        should_search = True

if should_search:
    with st.spinner("Brewing your recommendations…"):
        enriched = run_search(
            query=query_input, roast_level=roast_level, top_k=top_k,
            tokenizer=tokenizer, model=model, index=index,
            coffee_names=coffee_names, variance_scores=variance_scores, df=df,
        )
    st.session_state.results      = enriched
    st.session_state.last_query   = query_input
    st.session_state.last_roast   = roast_level
    st.session_state.last_top_k   = top_k
    st.session_state.searched_once = True


# ══════════════════════════════════════════════════════════════════════════════
# RESULTS / EMPTY STATE
# ══════════════════════════════════════════════════════════════════════════════
enriched = st.session_state.results

st.markdown('<div class="ci-divider"></div>', unsafe_allow_html=True)

if enriched:
    # ── Results header ──
    st.markdown(f"""
    <div class="ci-results-meta">
      <span class="count">{len(enriched)}</span>
      <span class="label">Flavor Matches</span>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.last_query:
        q_safe = st.session_state.last_query.replace("<", "&lt;").replace(">", "&gt;")
        st.markdown(f"""
        <div class="ci-query-echo">
          <span>Query</span>"{q_safe}"
        </div>
        """, unsafe_allow_html=True)

    # ── 2-column card grid ──
    results_per_row = 2
    for row_start in range(0, len(enriched), results_per_row):
        row_items = enriched[row_start : row_start + results_per_row]
        cols = st.columns(results_per_row)
        for col, r in zip(cols, row_items):
            with col:
                # Similarity 0→1 score expressed as a percentage
                score_pct = min(r["score"] * 100, 100.0)
                score_display = f"{score_pct:.1f}%"
                bar_width = f"{score_pct:.1f}%"

                risk_class = f"ci-risk-{r['risk_class']}"

                name_safe   = r["name"].title().replace("<", "&lt;").replace(">", "&gt;")
                review_safe = r["top_review"].replace("<", "&lt;").replace(">", "&gt;")
                roast_safe  = r["roast_level"].replace("<", "&lt;").replace(">", "&gt;")

                st.markdown(f"""
<div class="ci-card">
  <div class="ci-card-header">
    <h3>{name_safe}</h3>
    <span class="ci-roast-badge">{roast_safe}</span>
  </div>

  <blockquote class="ci-review">"{review_safe}"</blockquote>

  <div class="ci-match-row">
    <div class="ci-match-labels">
      <span class="label">Flavor Match</span>
      <span class="pct">{score_display}</span>
    </div>
    <div class="ci-bar-track">
      <div class="ci-bar-fill" style="width:{bar_width};"></div>
    </div>
  </div>

  <div class="ci-risk {risk_class}">
    <span class="dot"></span>
    {r['risk_label']} — {r['risk_desc']}
  </div>
</div>
""", unsafe_allow_html=True)

                with st.expander("Why this match?", expanded=False):
                    st.markdown(f"""
**Similarity score:** `{r['score']:.4f}`  
**Embedding variance:** `{r['variance']:.4f}`  
**Risk level:** {r['risk_label']}

The similarity score is the cosine distance between your query embedding and this
coffee's aggregate review embedding. Variance reflects how much reviewers' descriptions
diverge — higher variance means more unpredictable flavor experiences.
""")

    # ── Visual Analysis ────────────────────────────────────────────────────────
    st.markdown('<div class="ci-divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="ci-charts-header">Visual Analysis</p>', unsafe_allow_html=True)
    st.markdown('<p class="ci-section-label">Similarity &amp; Risk Breakdown</p>', unsafe_allow_html=True)

    chart_df = pd.DataFrame(enriched)
    chart_df["name_display"] = chart_df["name"].str.title().str[:28]
    chart_df["score_pct"]    = (chart_df["score"] * 100).clip(0, 100)

    col1, col2 = st.columns(2)

    with col1:
        fig_bar = px.bar(
            chart_df,
            x="score_pct",
            y="name_display",
            orientation="h",
            title="Flavor Match Score",
            color="score_pct",
            color_continuous_scale=["#e7e2da", "#fea054", "#6c2f00"],
            labels={"score_pct": "Match %", "name_display": ""},
        )
        fig_bar.update_layout(
            plot_bgcolor="#fef9f1",
            paper_bgcolor="#fef9f1",
            font_family="Plus Jakarta Sans",
            font_color="#1d1c17",
            coloraxis_showscale=False,
            margin=dict(l=0, r=10, t=44, b=10),
            title_font=dict(family="Newsreader", size=16, color="#1d1c17"),
            xaxis=dict(gridcolor="#f2ede5", range=[0, 100]),
            yaxis=dict(gridcolor="#f2ede5"),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        fig_scatter = px.scatter(
            chart_df,
            x="score_pct",
            y="variance",
            text="name_display",
            title="Match Score vs. Risk",
            color="variance",
            color_continuous_scale=["#174a2b", "#934b00", "#ba1a1a"],
            labels={"score_pct": "Match %", "variance": "Risk (Variance)"},
            size=[14] * len(chart_df),
        )
        fig_scatter.update_traces(textposition="top center", textfont_size=9)
        fig_scatter.update_layout(
            plot_bgcolor="#fef9f1",
            paper_bgcolor="#fef9f1",
            font_family="Plus Jakarta Sans",
            font_color="#1d1c17",
            coloraxis_showscale=False,
            margin=dict(l=0, r=10, t=44, b=10),
            title_font=dict(family="Newsreader", size=16, color="#1d1c17"),
            xaxis=dict(gridcolor="#f2ede5", range=[0, 100]),
            yaxis=dict(gridcolor="#f2ede5"),
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

elif st.session_state.searched_once:
    # ── No-results empty state ──────────────────────────────────────────────
    q_safe = st.session_state.last_query.replace("<", "&lt;").replace(">", "&gt;")
    st.markdown(f"""
<div class="ci-empty">
  <span class="big-q">?</span>
  <h2>No matches found.</h2>
  <p>
    No coffees matched <em>"{q_safe}"</em> with your current filters.
    Try simplifying your description or broadening the roast filter.
  </p>
  <p class="ci-section-label">Alternative Curations</p>
  <div class="ci-chips">
    <span class="ci-chip">Bright citrus light roast</span>
    <span class="ci-chip">Nutty dark roast</span>
    <span class="ci-chip">Berry-forward espresso</span>
    <span class="ci-chip">Floral tea-like light roast</span>
    <span class="ci-chip">Smoky morning brew</span>
  </div>
</div>
""", unsafe_allow_html=True)

else:
    # ── Pre-search state (landing) ──────────────────────────────────────────
    st.markdown("""
<div class="ci-empty">
  <span class="big-q">☕</span>
  <h2>Your sommelier awaits.</h2>
  <p>Describe what you're craving — in plain English — and we'll find your cup.</p>
  <p class="ci-section-label">Try one of these</p>
  <div class="ci-chips">
    <span class="ci-chip">Bright citrus floral light roast</span>
    <span class="ci-chip">Smoky chocolate dark roast</span>
    <span class="ci-chip">Berry-forward espresso</span>
    <span class="ci-chip">Nutty caramel medium roast</span>
    <span class="ci-chip">Floral jasmine tea-like</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<footer class="ci-footer">
  <p>
    © 2025 Caffe-In Editorial. All Rights Reserved.
    &nbsp;·&nbsp;
    <a href="#">The Ethos</a>
    <a href="#">Privacy</a>
    <a href="#">Contact</a>
  </p>
</footer>
""", unsafe_allow_html=True)
