games = [
    {
        "name": "Factorio",
        "hours": 800
    },
    {
        "name": "Satisfactory",
        "hours": 250
    },
    {
        "name": "RimWorld",
        "hours": 500
    }
]

most_played = games[0]

for game in games:
    if game["hours"] > most_played["hours"]:
        most_played = game

print(
    f'Most played game: {most_played["name"]} '
    f'({most_played["hours"]} hours)'
)