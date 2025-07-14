import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from fuzzywuzzy import process


df = pd.read_csv('books.csv')
df = df[['title', 'authors', 'description']].dropna().drop_duplicates().reset_index(drop=True)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()


def recommend(title, num_recommendations=5):
    choices = df['title'].tolist()
    matched_title, score = process.extractOne(title, choices)

    if score < 60:
        return [f"Book not found in dataset. Did you mean '{matched_title}'?"]

    idx = indices[matched_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    book_indices = [i[0] for i in sim_scores]
    recommended_books = df[['title', 'authors']].iloc[book_indices].reset_index(drop=True)

    return recommended_books

st.title("📚 Personalised Book Recommendation System")

user_input = st.text_input("Enter a book title you like:", "")

if st.button("Get Recommendations"):
    if user_input.strip() == "":
        st.warning("Please enter a book title to get recommendations.")
    else:
        results = recommend(user_input, num_recommendations=5)
        if isinstance(results, list):
            st.error(results[0])
        else:
            st.success(f"Books recommended based on '{user_input}':")
            for idx, row in results.iterrows():
                st.write(f"**{idx+1}. {row['title']}** by {row['authors']}")