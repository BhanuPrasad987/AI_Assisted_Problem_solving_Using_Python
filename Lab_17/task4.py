'''
Task: A streaming platform wants to analyze customer reviews.
Instructions:
- Standardize text (lowercase, remove HTML tags).
- Tokenize and encode reviews using AI-assisted methods (TF-IDF or embeddings).
- Handle missing ratings (fill with median).
- Normalize ratings (0–10 → 0–1 scale).
- Generate a before vs after summary report.'''
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler

# ----------------------
# 1. Load dataset
# ----------------------
df = pd.read_csv("movie_reviews-1.csv")

print("=== BEFORE CLEANING ===")
print(df.head())

# ----------------------
# 2. Standardize text
#    - Remove HTML tags
#    - Convert to lowercase
# ----------------------
def clean_text(text):
    if pd.isna(text):
        return ""
    text = BeautifulSoup(text, "html.parser").get_text()   # remove HTML
    text = text.lower()                                    # lowercase
    return text

df['clean_text'] = df['review_text'].apply(clean_text)

# ----------------------
# 3. Tokenize + TF-IDF vectorization
# ----------------------
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['clean_text'])

# 4. Handle missing ratings properly (no warning)
median_rating = df['rating'].median()
df['rating'] = df['rating'].fillna(median_rating)

# If you want to overwrite original review_text with cleaned text:
df['review_text'] = df['clean_text']
# ----------------------
# 5. Normalize ratings (0–10 → 0–1 scale)
# ----------------------
scaler = MinMaxScaler()
df['rating_normalized'] = scaler.fit_transform(df[['rating']])

# ----------------------
# 6. Summary before vs after
# ----------------------
summary = {
    "Total rows before cleaning": len(df),
    "Missing ratings filled with": median_rating,
    "TF-IDF feature count": tfidf_matrix.shape[1],
}

print("\n=== CLEANING SUMMARY ===")
for key, value in summary.items():
    print(f"{key}: {value}")

print("\n=== AFTER CLEANING (HEAD) ===")
print(df[['review_id','clean_text','rating','rating_normalized']].head())

# Optional: Save cleaned dataset
df.to_csv("reviews_cleaned.csv", index=False)

