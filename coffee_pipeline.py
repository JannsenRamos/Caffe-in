import re
import unicodedata

import numpy as np
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df

def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    required_cols = ['coffee_name', 'score', 'review', 'roast_level']
    assert not df.empty, "Dataset is empty"
    assert all(col in df.columns for col in required_cols), \
        f"Missing columns! Required: {required_cols}, Found: {list(df.columns)}"
    return df

def prepare_kaggle(kaggle_filepath: str) -> pd.DataFrame:
    kaggle_df = pd.read_csv(kaggle_filepath)

    kaggle_df = pd.melt(
                kaggle_df,
                id_vars=["name", "roast", "rating"],  
                value_vars=["desc_1", "desc_2", "desc_3"],          
                value_name="review"                                 
                )

    kaggle_df = kaggle_df.rename(columns={
        "name": "coffee_name",
        "roast": "roast_level",
        "rating": "score"
    })

    kaggle_df = kaggle_df.drop(columns=["variable"])

    kaggle_df = kaggle_df[kaggle_df["review"].notna() & (kaggle_df["review"].str.strip() != "")]

    kaggle_df = kaggle_df[["coffee_name", "roast_level", "score", "review"]]

    return kaggle_df

def load_and_merge_kaggle(df: pd.DataFrame, kaggle_filepath: str) -> pd.DataFrame:
    kaggle_df = pd.read_csv(kaggle_filepath)

    kaggle_df = kaggle_df[["coffee_name", "review", "roast_level"]]
    merged_df = pd.concat([df, kaggle_df], ignore_index=True)

    return merged_df

def filter_by_review_density(df: pd.DataFrame, min_reviews: int = 3) -> pd.DataFrame:
    review_count = df.groupby('coffee_name')['review'].size()
    coffee_with_many_reviews = review_count[review_count >= min_reviews].index

    filtered_df = df[df["coffee_name"].isin(coffee_with_many_reviews)]

    return filtered_df

def normalize_name(df: pd.DataFrame) -> pd.DataFrame:
    df["coffee_name"] = (
        df["coffee_name"]
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9\s]", "", regex=True)
        .str.replace(r"\s+", " ", regex=True)  # collapse multiple spaces into one
    )
    return df

def apply_text_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df["review"] = df["review"].apply(clean_text)
    return df



def clean_text(review: str):
    if review is None or pd.isna(review):
        return ""
    else:
        review = unicodedata.normalize("NFKD", review).encode("ascii", "ignore").decode("utf-8")
        review = review.strip()
        review = re.sub(r"\s+", " ", review).strip()
        return review


def build_pipeline(filepath: str, kaggle_filepath: str) -> pd.DataFrame:
    df = load_data(filepath)

    df = validate_schema(df)

    df = normalize_name(df)

    kaggle_df = prepare_kaggle(kaggle_filepath)

    kaggle_df = normalize_name(kaggle_df)

    overlap_mask = kaggle_df["coffee_name"].isin(df["coffee_name"])
    kaggle_overlap = kaggle_df[overlap_mask]
    merged_df = pd.concat([df, kaggle_overlap], ignore_index=True)

    filtered_df = filter_by_review_density(merged_df)

    filtered_df = apply_text_cleaning(filtered_df)

    return filtered_df





