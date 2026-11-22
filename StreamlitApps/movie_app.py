import requests
import streamlit as st
import random
import json

def save_movies():
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)
def load_movies():
    try:
        with open("movies.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
            return [
            {
                "name": "Interstellar", 
                "rating": 8.7
            },
            {
                "name": "The Matrix", 
                "rating": 8.7
            },
            {
                "name": "Inception", 
                "rating": 8.8
            },
            {
                "name": "The Dark Knight", 
                "rating": 9.0
            },
            {
                "name": "Alien", 
                "rating": 8.4
            }
            ]
movies = load_movies()
api_key = "b542e990"
def get_movie_data(movie):
    url = (
        f"https://www.omdbapi.com/"
        f"?apikey={api_key}"
        f"&t={movie}"
    )
    response = requests.get(url)
    return response.json()
def display_movie(data):
    st.subheader(data["Title"])
    col1, col2 = st.columns(2)
    with col1:
        st.image(data["Poster"])
        if data["Poster"] != "N/A":
            st.image(data["Poster"])
    with col2:
        st.write(f"**Year:** {data['Year']}")
        st.write(f"**Genre:** {data['Genre']}")
        st.write(f"**Director:** {data['Director']}")
        st.write(f"**IMDB Rating:** {data['imdbRating']}")

    st.write("### Plot")
    st.write(data["Plot"])
st.title("🎬 Movie Database")
movie = st.text_input("Search for a movie")
if st.button("Search"):
    data = get_movie_data(movie)
    if data["Response"] == "True":
     display_movie(data)
    else:
        st.error("Movie not found.")
if st.button("Random Movie"):
    movie = random.choice(movies)
    data = get_movie_data(movie["name"])
    display_movie(data)
st.sidebar.title("Movie Library")
sorted_movies = sorted(
    movies,
    key=lambda movie: movie["rating"],
    reverse=True
)
for index, movie in enumerate(sorted_movies):
        if st.sidebar.button(
            f"{movie['name']} ⭐ {movie['rating']}",
            key=f"movie_{index}"
        ):
            data = get_movie_data(movie["name"])
            display_movie(data)