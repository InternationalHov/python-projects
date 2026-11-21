import requests
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

def search_movie(movie):
    data = get_movie_data(movie)

    if data["Response"] == "True":

        print(f"\nTitle: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"Genre: {data['Genre']}")
        print(f"Director: {data['Director']}")
        print(f"Rating: {data['imdbRating']}")
        print("\nPlot:")
        print(data['Plot'])

    else:
        print("\nMovie not found.")
while True:
    print("\n=== Movie Search ===")
    print("1. Search for a movie")
    print("2. Random movie suggestion")
    print("3. Add a movie to the list")
    print("4. View all movies")
    print("5. Delete a movie from the list")
    print("6. Highest rated Movie")
    print("7. Search movie list")
    print("8. Top 5 Movies")
    print("9. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        movie = input("\nEnter the movie title: ")
        search_movie(movie)
    elif choice == "2":
        movie = random.choice(movies)
        print(f"\nRandom movie suggestion: {movie['name']}")
        search_movie(movie['name'])
    elif choice == "3":
        movie = input("\nEnter the movie title: ")
        data = get_movie_data(movie)
        if data["Response"] == "True":
            if data["imdbRating"] != "N/A":
                already_exists = False
                for saved_movie in movies:
                    if (
                        saved_movie["name"].lower()
                        == data["Title"].lower()
                    ):
                        already_exists = True
                        break
                if already_exists:
                    print("Movie already exists.")
                else:
                    movies.append(
                        {
                        "name": data["Title"],
                        "rating": float(data["imdbRating"])
                        }
                    )
                    save_movies()
                    print(f"{data['Title']} added.")
            else:
                print("This movie doesn't have an IMDb rating.")
        else:
            print("Movie not found.")
    elif choice == "4":
        print("\n==Movie Suggestions==")
        for movie in movies:
            print(
                f"{movie['name']} "
                f"({movie['rating']})"
            )
    elif choice == "5":
        print("\n=== Delete Movie ===")
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie['name']}")
        delete_choice = int(
        input("\nChoose a movie to delete: ")
        )
        if 1 <= delete_choice <= len(movies):
            removed = movies.pop(delete_choice - 1)
            save_movies()
            print(f"{removed['name']} removed.")
        else:
            print("Invalid choice. Please try again.")
    elif choice == "6":

        highest_rated = None

        for movie in movies:
  
            if "rating" not in movie:
                continue

            if (
                highest_rated is None
                or movie["rating"] > highest_rated["rating"]
            ):
                highest_rated = movie

        if highest_rated:

            print(
                f"Highest rated movie: "
                f"{highest_rated['name']} "
                f"({highest_rated['rating']})"
            )

        else:
            print("No rated movies found.")
    elif choice == "7":
            search = input("\nEnter a movie name to search for: ").lower()
            found = False
            for movie in movies:
                if search in movie["name"].lower():
                    print(
                        f"{movie['name']}" 
                        f"({movie['rating']})"
                    )
                    found = True
            if not found:
                print(f"No movies found matching '{search}'.")
    elif choice == "8":
        sorted_movies = sorted(
            movies, 
            key=lambda movie: movie["rating"], 
            reverse=True
        )
        print("\n=== Top 5 movies by rating ===")
        for movie in sorted_movies[:5]:
            print(
                f"{movie['name']} "
                f"({movie['rating']})"
            )              
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, 4, 5, 6, 7, 8 or 9.")