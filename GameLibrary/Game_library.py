import json

def save_games():
    with open("games.json", "w") as file:
        json.dump(games, file, indent=4)

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
        
games = load_games()

while True:

    print("\n=== Game Library ===")
    print("1. View Games")
    print("2. Add Game")
    print("3. Edit Hours")
    print("4. Most Played")
    print("5. Delete Game")
    print("6. Total Hours")
    print("7. Sort by Hours")
    print("8. Search Games")
    print("9. Quit")

    choice = input("\nChoose an option: ")
    if choice == "1":
        print("\n=== Game List ===")
        for game in games:
            print(f"{game['name']} - {game['hours']} hours")
    elif choice == "2":
        name = input("Enter the name of the game: ")
        hours = int(input("Enter the number of hours played: "))
        games.append({"name": name, "hours": hours})
        save_games()
        print(f"{name} added to your game library.")
    elif choice == "3":
        print("\n=== Edit Hours ===")
        for index, game in enumerate(games, start=1):
            print(f"{index}. {game['name']} - {game['hours']} hours")
        edit_choice = int(input("\nChoose a game to edit: "))
        if 1 <= edit_choice <= len(games):
            new_hours = int(input("Enter the new number of hours played: "))
            games[edit_choice - 1]["hours"] = new_hours
            save_games()
            print(f"Updated hours for {games[edit_choice - 1]['name']}.")
        else:
            print("Invalid choice. Please try again.")
    elif choice == "4":
        most_played = games[0]
        for game in games:
            if game["hours"] > most_played["hours"]:
                most_played = game
        print(
            f'Most played game: '
            f'{most_played["name"]} '
            f'({most_played["hours"]} hours)'
        )
        if not games:
            print("No games in the library.")
    elif choice == "5":
        print("\n=== Delete Game ===")
        for index, game in enumerate(games, start=1):
            print(f"{index}. {game['name']}")
        delete_choice = int(
        input("\nChoose a game to delete: ")
    )
        if 1 <= delete_choice <= len(games):
            removed = games.pop(delete_choice - 1)
            save_games()
            print(f"{removed['name']} removed.")
        else:
            print("Invalid choice. Please try again.")
    elif choice == "6":
        total_hours = 0
        for game in games:
            total_hours += game["hours"]
        print(f"Total hours played: {total_hours}")
    elif choice == "7":
        sorted_games = sorted(
            games, 
            key=lambda game: game["hours"], 
            reverse=True
            )
        print("\n=== Games Sorted by Hours ===")
        for game in sorted_games:
            print(f"{game['name']} - {game['hours']} hours")
    elif choice == "8":
        search = input("\nEnter a game name to search for: ").lower()
        found = False
        for game in games:
            if search in game["name"].lower():
                print(f" - {game['name']} ({game['hours']} hours)")
                found = True
        if not found:
            print(f"No games found matching '{search}'.")
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")