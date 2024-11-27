# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kuXtwMVznkbvinauYLJzD_a1g_0_vDPE
"""

pip install streamlit

import streamlit as st
import pandas as pd

# Load the dataset with Book Links and Images
df = pd.read_csv("/content/final_books_data.csv")  # Ensure this file has Book_Link and Book_Image filled

# Function to fetch recommendations (based on cosine similarity or clustering)
def recommend_books(selected_title, num_recommendations=5):
    if selected_title in df['Title'].values:
        index = df[df['Title'] == selected_title].index[0]
        recommendations = sorted(
            list(enumerate(cosine_sim[index])), key=lambda x: x[1], reverse=True
        )[1 : num_recommendations + 1]
        return [df.iloc[i[0]] for i in recommendations]
    return []

# Streamlit Web App
st.title("Book Recommendation System")

# Search bar for book titles
book_titles = df['Title'].tolist()
selected_book = st.selectbox("Search for a Book:", options=book_titles)

if st.button("Recommend"):
    if selected_book:
        st.subheader(f"Top Recommendations for '{selected_book}':")
        recommendations = recommend_books(selected_book)

        for book in recommendations:
            st.image(book['Book_Image'], width=150)  # Display book image
            st.write(f"**Title:** {book['Title']}")
            st.write(f"**Author ID:** {book['AuthID']}")
            st.write(f"**Rating:** {book['Rating']}")
            st.write(f"**Genre:** {book['Genre']}")
            st.write(f"**Price:** ₹{book['Price']}")
            st.markdown(f"[More Info]({book['Book_Link']})")  # Hyperlink to book info
    else:
        st.error("Please select a valid book.")

