import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API_URL = "http://127.0.0.1:8000/search"

def get_risk_label(variance: float) -> str:
    pass

def search_coffees(query: str, top_k: int, roast_level: str) -> list:
    pass

def render_results(results: list) -> None:
    pass

def render_charts(results: list) -> None:
    pass

# main app
st.title("☕ Caffe-In")
st.write("Find your perfect coffee by describing what you're looking for.")

# your UI code here