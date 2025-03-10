import os
import joblib  # Import joblib for loading .pkl files
import streamlit as st

BASE_DIR = os.getcwd()  # Get the current working directory

# Function to safely load a pickle file using joblib
def load_pkl_file(filename):
    file_path = os.path.join(BASE_DIR, filename)
    if os.path.exists(file_path):
        return joblib.load(file_path)  # Use joblib instead of pickle
    else:
        st.error(f"❌ Error: `{filename}` not found in `{BASE_DIR}`. Please check if the file is uploaded.")
        return None

# Load files safely
df_new = load_pkl_file("df_new.pkl")
similarity_scores = load_pkl_file("similarity_scores.pkl")

# Stop execution if files are missing
if df_new is None or similarity_scores is None:
    st.stop()

st.title("📚 Book Recommendation System")
selected_book = st.selectbox("Choose a book", df_new['Title'].values)

def recommend_books(book_name):
    if book_name not in df_new['Title'].values:
        return ["Book not found. Please try another one."]
    
    book_index = df_new[df_new['Title'] == book_name].index[0]
    distances = similarity_scores[book_index]
    recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_books = [df_new.iloc[i[0]]['Title'] for i in recommended_indices]
    return recommended_books

if st.button("Recommend"):
    recommendations = recommend_books(selected_book)
    st.subheader("📖 Recommended Books:")
    for book in recommendations:
        st.write(f"📌 {book}")
