import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎥",
    layout="wide"
)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
movies = pickle.load(open('movies.pkl', 'rb'))
#similarity = pickle.load(open('similarity.pkl', 'rb'))
vectors = pickle.load(open('vectors.pkl','rb'))
# ------------------------------------------------
# FETCH POSTER FUNCTION
# ------------------------------------------------
def fetch_poster(movie_id):

    api_key = "e64f523fb9adcab0e133d6109cbdd16f"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    data = requests.get(url)

    data = data.json()

    poster_path = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path

# ------------------------------------------------
# RECOMMEND FUNCTION
# ------------------------------------------------
# def recommend(movie):

#     movie_index = movies[movies['title'] == movie].index[0]

#     distances = similarity[movie_index]

#     movies_list = sorted(
#         list(enumerate(distances)),
#         reverse=True,
#         key=lambda x: x[1]
#     )[1:6]

#     recommended_movies = []
#     recommended_posters = []

#     for i in movies_list:

#         movie_id = movies.iloc[i[0]].movie_id

#         recommended_movies.append(
#             movies.iloc[i[0]].title
#         )

#         recommended_posters.append(
#             fetch_poster(movie_id)
#         )

#     return recommended_movies, recommended_posters
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    similarity = cosine_similarity(
        vectors[movie_index].reshape(1,-1),
        vectors
    )

    distances = similarity[0]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters

# ------------------------------------------------
# TITLE
# ------------------------------------------------
st.title('🎬 Movie Recommender System')

# ------------------------------------------------
# SELECT MOVIE
# ------------------------------------------------
selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

# ------------------------------------------------
# BUTTON
# ------------------------------------------------
if st.button('Recommend'):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])