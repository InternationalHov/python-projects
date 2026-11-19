import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=53.38"
    "&longitude=-1.47"
    "&current=temperature_2m"
)

response = requests.get(url)

data = response.json()

temp = data["current"]["temperature_2m"]

print("== Weather Checker ==")
print(f"Current temperature in Sheffield is: {temp}°C")