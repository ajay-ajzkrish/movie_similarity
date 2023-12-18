import pickle
import streamlit as st
import requests
import pandas

def recommend(movie):
    movie = movie.lower()
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title.title())

    return recommended_movie_names


def recommend_plot(movie):
    movie = movie.lower()
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_plot[index])),reverse=True,key = lambda x: x[1])
    recommended_movie_names_plot = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names_plot.append(movies.iloc[i[0]].title.title())

    return recommended_movie_names_plot

st.write("[LinkedIn](https://www.linkedin.com/in/ajzkrish/)"," | ","[Github](https://github.com/ajay-ajzkrish)")
st.title('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
similarity_plot = pickle.load(open('similarity_plot.pkl','rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    st.header("Here are a few suggestion")
    st.text(recommended_movie_names[0])
    st.text(recommended_movie_names[1])    
    st.text(recommended_movie_names[2])
    st.text(recommended_movie_names[3])
    st.text(recommended_movie_names[4])    
if st.button('Show Recommendation based on Plot of the movie'):
    recommended_movie_names_plot = recommend_plot(selected_movie)
    st.header("Here are a few suggestion")
    st.text(recommended_movie_names_plot[0])
    st.text(recommended_movie_names_plot[1])    
    st.text(recommended_movie_names_plot[2])
    st.text(recommended_movie_names_plot[3])
    st.text(recommended_movie_names_plot[4])    

