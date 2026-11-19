import requests

while True:

    print("\n=== Advice Machine ===")
    print("1. Get Advice")
    print("2. About")
    print("3. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        response = requests.get(
            "https://api.adviceslip.com/advice"
        )

        data = response.json()

        print("\nAdvice:")
        print(data["slip"]["advice"])

    elif choice == "2":

        print("\nAdvice Machine v1.0.\nCreated by Craig Huggins.")

    elif choice == "3":
        
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, or 3.")