import streamlit as st
import pickle
import pandas as pd

# Load the pickled data
movies_list = pd.read_pickle(open("movies.pkl", "rb"))

# Access the 'title' column if it's a DataFrame
if isinstance(movies_list, pd.DataFrame) and 'title' in movies_list.columns:
    movie_titles = movies_list['title'].values

st.title("Movie Recommendation System")

# Provide the movie selection
option = st.selectbox(
    "Select a movie:",
    movie_titles,
)

st.write("You selected:", option)
