# 🎬 Movie Recommendation System

A content-based movie recommender system that suggests similar movies using tag-based natural language processing (NLP) and cosine similarity.

## 🛠 Tools & Libraries
- Python (Jupyter Notebook)
- Pandas, NumPy, scikit-learn
- Streamlit (for deployment)

## 🔍 How It Works
- The dataset is cleaned and preprocessed to extract important textual features like genres, cast, keywords, and overview.
- A new 'tags' column is created by combining relevant features.
- Cosine similarity is calculated on the tag vectors to find and recommend similar movies.
- Since it’s tag-based, results are **static** — they do not change with user feedback or ratings.

## 🚀 Try the App
👉 [Launch the Movie Recommender (Streamlit)](https://hardik-jain-movie-recommendation-system.streamlit.app/)

## 📂 Dataset Source
Typically based on TMDB movie metadata (can include title, genres, overview, cast, crew, etc.)

## ✅ Outcome
This project demonstrates the fundamentals of building a static recommendation engine using text data and vector similarity — a foundational skill in content-based filtering for data science.
