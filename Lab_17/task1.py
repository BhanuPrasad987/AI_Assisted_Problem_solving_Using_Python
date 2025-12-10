'''Task: Clean raw social media posts dataset.
Instructions:
- Remove stopwords, punctuation, and special symbols from post text.
- Handle missing values in likes and shares columns.
- Convert timestamp to datetime and extract features (hour, weekday).
- Detect and remove spam/duplicate posts.
'''
import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv("social_media.csv")

print("=== RAW DATA (HEAD) ===")
print(df.head())

# ---------------------------
# 1. CLEAN POST TEXT
#    - Remove HTML
#    - Lowercase
#    - Remove punctuation
#    - Remove stopwords (custom list)
# ---------------------------

stopwords = {"this", "is", "a", "the", "an", "and", "or", "to", "of", "for"}

def clean_text(text):
    if pd.isna(text):
        return ""

    text = BeautifulSoup(text, "html.parser").get_text()  # remove HTML
    text = text.lower()                                    # lowercase
    text = re.sub(r'[^a-z0-9\s]', ' ', text)               # remove punctuation

    # remove stopwords
    words = [w for w in text.split() if w not in stopwords]
    return " ".join(words)

df["clean_text"] = df["post_text"].apply(clean_text)
df["post_text"] = df["clean_text"]


# ---------------------------
# 2. HANDLE MISSING VALUES
# ---------------------------
df["likes"] = df["likes"].fillna(0)
df["shares"] = df["shares"].fillna(0)

# ---------------------------
# 3. PROCESS TIMESTAMP
# ---------------------------
df["timestamp"] = pd.to_datetime(df["timestamp"], dayfirst=True)
df["hour"] = df["timestamp"].dt.hour
df["weekday"] = df["timestamp"].dt.day_name()

# ---------------------------
# 4. REMOVE DUPLICATES AND SPAM
# ---------------------------

# Remove duplicate posts
df = df.drop_duplicates(subset=["clean_text"])

# Spam detection (simple version)
def is_spam(text):
    if len(text) <= 3:
        return True
    if re.search(r"(.)\1{4,}", text):  # repeated characters
        return True
    return False

df = df[~df["clean_text"].apply(is_spam)]

# ---------------------------
# FINAL OUTPUT
# ---------------------------
print("\n=== CLEANED DATA (HEAD) ===")
print(df.head())

df.to_csv("social_media_cleaned.csv", index=False)
