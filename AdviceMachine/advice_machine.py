import requests

def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json()
    print("\nAdvice:")
    print(data["slip"]["advice"])

def show_weather(city, latitude, longitude):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m"
    )

    response = requests.get(url)
    data = response.json()
    
    temp = data["current"]["temperature_2m"]

    return city, temp 

def weather_opinion(temp):
    if temp < 10:
        return "Cold today."
    elif temp < 20:
        return "Bit chilly today."
    else:
        return "Nice and warm today."
    
cities = {
    "1": ("Sheffield", 53.38, -1.47),
    "2": ("London", 51.5074, -0.1278),
    "3": ("Manchester", 53.4808, -2.2451),
    "4": ("Edinburgh", 55.9533, -3.1883)
}

while True:

    print("\n=== Information Hub ===")
    print("1. Get Advice")
    print("2. Get Weather")
    print("3. About")
    print("4. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        get_advice()
    elif choice == "2":
        print("\n1. Sheffield")
        print("2. London")
        print("3. Manchester")
        print("4. Edinburgh")
        city_choice = input("\nChoose a city: ")
        if city_choice in cities:
            city, latitude, longitude = cities[city_choice]
            city, temp = show_weather(city, latitude, longitude)
            print(f"\nCurrent temperature in {city} is {temp}°C")
            print("\nWeather opinion:")
            print(weather_opinion(temp))
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
    elif choice == "3":
        print("\nInformation Hub v1.0")
        print("Created by Craig Huggins")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")