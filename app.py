import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np


def fetch_poster(id_of_movie):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{id_of_movie}?api_key=33414a62315a18a33a3cbd492ef6abcd&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        id_of_movie = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        # FETCH POSTER FROM API
        recommended_movies_posters.append(fetch_poster(id_of_movie))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity1 = pickle.load(open('similarity1.pkl', 'rb'))
similarity2 = pickle.load(open('similarity2.pkl', 'rb'))
similarity3 = pickle.load(open('similarity3.pkl', 'rb'))
similarity4 = pickle.load(open('similarity4.pkl', 'rb'))
similarity5 = pickle.load(open('similarity5.pkl', 'rb'))
similarity6 = pickle.load(open('similarity6.pkl', 'rb'))
similarity7 = pickle.load(open('similarity7.pkl', 'rb'))
similarity8 = pickle.load(open('similarity8.pkl', 'rb'))
similarity9 = pickle.load(open('similarity9.pkl', 'rb'))
similarity1to3 = np.concatenate((similarity1,similarity2,similarity3), axis=0)
similarity4to6 = np.concatenate((similarity4,similarity5,similarity6), axis=0)
similarity7to9 = np.concatenate((similarity7,similarity8,similarity9), axis=0)
similarity = np.concatenate((similarity1to3,similarity4to6,similarity7to9), axis=1)
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    "Please enter the name of a movie that you've enjoyed watching to get recommendations similar to it",
    movies['title'].values)

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