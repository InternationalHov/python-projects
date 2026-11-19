import requests

while True:
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json()

    print(data)
    print("Today's advice:")
    print(data["slip"]["advice"])

    again = input("\nAnother piece of advice? (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break