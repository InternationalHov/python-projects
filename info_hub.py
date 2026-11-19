import requests

while True:

    print("\n=== Information Hub ===")
    print("1. Get Advice")
    print("2. Get Weather")
    print("3. About")
    print("4. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        response = requests.get("https://api.adviceslip.com/advice")
        data = response.json()
        print("\nAdvice:")
        print(data["slip"]["advice"])
    elif choice == "2":
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=53.38"
            "&longitude=-1.47"
            "&current=temperature_2m"
        )
        response = requests.get(url)
        data = response.json()
        temp = data["current"]["temperature_2m"]
        print(f"Current temperature in Sheffield is: {temp}°C")
    elif choice == "3":
        print("\nInformation Hub v1.0")
        print("Created by Craig Huggins")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")
