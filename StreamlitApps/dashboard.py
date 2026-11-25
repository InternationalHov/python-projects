import streamlit as st
import requests
import random
import json
st.set_page_config(
    page_title="Craig's Dashboard",
    page_icon="🏠"
    )
def get_weather(latitude, longitude):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m"
    )
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"]
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
def save_movies():
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)
movies = load_movies()
api_key = "b542e990"
def load_games():
    try:
        with open("games.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
            return [
            {
                "name": "Factorio",
                "hours": 800
            },
            {
                "name": "Satisfactory",
                "hours": 250
            }
        ]
def save_games():
    with open("games.json", "w") as file:
        json.dump(games, file, indent=4)
games = load_games()
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
        if data["Poster"] != "N/A":
            st.image(data["Poster"])
    with col2:
        st.write(f"**Year:** {data['Year']}")
        st.write(f"**Genre:** {data['Genre']}")
        st.write(f"**Director:** {data['Director']}")
        st.write(f"**IMDB Rating:** {data['imdbRating']}")
    st.write("### Plot")
    st.write(data["Plot"])
cities = {
    "Sheffield": (53.38, -1.47),
    "London": (51.5074, -0.1278),
    "Manchester": (53.4808, -2.2451),
    "Edinburgh": (55.9533, -3.1883)
        }
page = st.sidebar.selectbox(
    "Choose a section",
    [
    "🏠 Home",
    "🎬 Movie Database",
    "🎮 Game Library",
    "🌦 Weather",
    "💡 Advice"
    ]
        )
if page == "🏠 Home":
    st.header("🏠 Home")
    st.write(
        "Welcome to your personal dashboard."
    )
    col1,col2 = st.columns(2)
    with col1:
        st.metric(
        "Movies Saved",
        len(movies)
    )
    with col2:
        st.metric(
        "Games Saved",
        len(games)
    )
elif page == "🎬 Movie Database":
    st.header ("🎬 Movie Database")
    movie = st.text_input("Search for a movie")
    if st.button("🔍 Search Movie"):
        data = get_movie_data(movie)
        if data["Response"] == "True":
            display_movie(data)
        else:
            st.error("Movie not found.")
    if st.button ("🎲 Random Movie"):
        movie = random.choice(movies)
        data = get_movie_data(movie["name"])
        display_movie(data)
    st.write("---")
    st.subheader("⭐ Saved Movies")
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )
    for index, movie in enumerate(sorted_movies):
        if st.button(
            f"{movie['name']} ⭐ {movie['rating']}",
            key=f"movie_{index}"
        ):
            data = get_movie_data(movie["name"])
            display_movie(data)
elif page == "🎮 Game Library":

    st.header("🎮 Game Library")

    st.write("---")

    most_played = games[0]

    for game in games:

        if game["hours"] > most_played["hours"]:

            most_played = game

    total_hours = sum(
        game["hours"] for game in games
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Hours",
            total_hours
        )

    with col2:

        st.metric(
            "Most Played",
            most_played["name"]
        )

    with col3:

        st.metric(
            "Games Saved",
            len(games)
        )

    st.subheader("🎮 Games")

    st.table(games)

    search_game = st.text_input(
        "Search Games"
    )

    if search_game:

        for game in games:

            if search_game.lower() in game["name"].lower():

                st.write(
                    f"{game['name']} "
                    f"({game['hours']} hours)"
                )

    st.subheader("➕ Add Game")

    new_game = st.text_input("Game Name")

    hours = st.number_input(
        "Hours Played",
        min_value=0
    )

    if st.button("Add Game"):

        games.append(
            {
                "name": new_game,
                "hours": hours
            }
        )

        save_games()

        st.success(f"{new_game} added!")
elif page == "🌦 Weather":
    st.header ("🌦 Weather")
    city = st.selectbox(
        "Choose a city",
        list(cities.keys())
    )
    latitude, longitude = cities[city]
    temp = get_weather(
            latitude,
            longitude
    )
    st.metric(
        label=f"{city} Temperature",
        value=f"{temp}°C"
    )
    if temp < 10:
        st.info("🥶 Cold today.")
    elif temp < 20:
        st.info("🧥 Bit chilly today.")
    else:
        st.success("😎 Nice and warm today.")
elif page == "💡 Advice":
    st.header ("💡 Advice")
    if st.button("Get Advice"):
        response = requests.get(
            "https://api.adviceslip.com/advice"
        )
        data = response.json()
        st.success(data["slip"]["advice"])