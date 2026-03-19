#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt


# In[2]:


filepath = r"C:\Users\Lenovo\Documents\GitHub\Coffee_Reco_System\data\raw\coffee_reviewsV2.csv"
kaggle_filepath= r"C:\Users\Lenovo\Documents\GitHub\Coffee_Reco_System\data\raw\kaggle_coffee_analysis.csv"


# In[3]:


df = pd.read_csv(filepath)


# In[4]:


df.head(5)


# In[5]:


counts = df.groupby('coffee_name')['review'].size()
print("Max reviews: ",counts.max())
print("Max reviews: ",counts.min())
print("Coffees with only 1 review: ", (counts == 1).sum())


# In[6]:


df.groupby('coffee_name').size().describe()


# In[7]:


reviews = df.groupby('coffee_name').size()
print("Coffee with 1 review:", (reviews == 1).sum())
print("Coffee with 3 reviews:", (reviews >= 3).sum())
print("Coffee with over 5 reviews:", (reviews >= 5).sum())


# In[8]:


print(df.shape)
print(df['coffee_name'].nunique())


# In[9]:


kaggle_df = pd.read_csv(r"C:\Users\Lenovo\Documents\GitHub\Coffee_Reco_System\data\raw\kaggle_coffee_analysis.csv")


# In[10]:


overlap = set(df['coffee_name'].str.lower().str.strip()) & set(kaggle_df['name'].str.lower().str.strip())
print(len(overlap))


# In[11]:


kaggle_df = pd.read_csv(kaggle_filepath)
print(kaggle_df.columns.tolist())
print(kaggle_df.head(2))
kaggle_df.shape[0]


# In[12]:


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


# In[13]:


def normalize_name(df: pd.DataFrame) -> pd.DataFrame:
    df["coffee_name"] = (
        df["coffee_name"]
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9\s]", "", regex=True)
        .str.replace(r"\s+", " ", regex=True)  # collapse multiple spaces into one
    )
    return df


# In[27]:


def apply_text_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df["review"] = df["review"].apply(clean_text)
    return df


# In[39]:


import re
def clean_text(review: str):
    if review is None or pd.isna(review):
        return ""
    else:
        review = unicodedata.normalize("NFKD", review).encode("ascii", "ignore").decode("utf-8")
        review = review.strip()
        review = re.sub(r"\s+", " ", review).strip()
        return review


# In[40]:


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


# In[41]:


final_df = build_pipeline(filepath, kaggle_filepath)
print(final_df.shape)
print(final_df["coffee_name"].nunique())
print(final_df.groupby("coffee_name").size().describe())


# In[42]:


final_df = final_df.drop(columns=["url", "review_date"])
final_df["score"] = pd.to_numeric(final_df["score"], errors="coerce")
final_df["roast_level"] = final_df["roast_level"].fillna("Unknown")


# In[43]:


print(final_df.isnull().sum())
print(final_df.dtypes)
print(final_df["roast_level"].value_counts())


# In[44]:


final_df.to_parquet("coffee_clean.parquet", index=False)


# In[45]:


final_df["review_length"] = final_df["review"].str.split().str.len()
print(final_df["review_length"].describe())


# In[46]:


import re

# check for HTML artifacts
print(final_df["review"].str.contains(r"<.*?>", regex=True).sum())

# check for URLs
print(final_df["review"].str.contains(r"http", regex=True).sum())

# check for excessive punctuation or special characters
print(final_df["review"].str.contains(r"[^a-zA-Z0-9\s,.\-']", regex=True).sum())

# show samples of reviews with special characters
mask = final_df["review"].str.contains(r"[^a-zA-Z0-9\s,.\-']", regex=True)
print(final_df[mask]["review"].head(10).values)


# In[47]:


final_df = build_pipeline(filepath, kaggle_filepath)
print(final_df["review"].head(5).values)


# In[ ]:





# In[ ]:




