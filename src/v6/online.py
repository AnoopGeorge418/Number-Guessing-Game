import requests
import random

BASE_URL = "http://127.0.0.1:5000"

secret_number  = random.randint(1, 100)

def onlinePlay():
    print("\n===== ONLINE NUMBER GUESS =====\n")
    # Join / Create Game
    try:
        res = requests.post(f"{BASE_URL}/start")
        data = res.json()
        print(data["message"])
    except Exception:
        print("Server not reachable.")
        return
    
    total_attempts = 5
    attempts = 0

    while attempts < total_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        try:
            res = requests.post(
                f"{BASE_URL}/guess",
                json={"guess": guess}
            )
            result = res.json()
        except Exception:
            print("Connection lost.")
            return

        print("Result:", result["result"])
        attempts += 1

        if result["result"] == "Correct":
            print("🎉 You Won Online!\n")
            return

        print(f"Attempts left: {total_attempts - attempts}")

    print("💀 You Lost!")

