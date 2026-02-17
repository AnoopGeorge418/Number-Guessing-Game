import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


def ask_ai(prompt):
    payload = {
        "model": "HuggingFaceH4/zephyr-7b-beta",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 20,
        "temperature": 0.5
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    data = response.json()

    # handle loading/error
    if isinstance(data, dict) and "error" in data:
        print("AI waking up... waiting 15 sec")
        time.sleep(15)
        return ask_ai(prompt)

    try:
        return data["choices"][0]["message"]["content"]
    except:
        return "50"


def extract_number(text):
    digits = ''.join(filter(str.isdigit, text))
    return int(digits) if digits else 50


def aiVsAi():
    print("\n========== AI VS AI ==========\n")
    print("AI Alpha picking secret number...\n")

    # AI A picks secret
    secret_text = ask_ai("Pick a number between 1 and 100. Only output number.")
    secret_number = extract_number(secret_text)

    print("AI Alpha has chosen a secret number.")
    print("(Hidden from AI Beta)\n")

    low = 1
    high = 100
    attempts = 0

    while True:
        attempts += 1

        print(f"\n--- Round {attempts} ---")

        guess_text = ask_ai(
            f"Guess ONE number between {low} and {high}. Only output number."
        )
        guess = extract_number(guess_text)

        print(f"AI Beta guesses: {guess}")

        if guess > secret_number:
            print("System: Too High")
            high = guess - 1

        elif guess < secret_number:
            print("System: Too Low")
            low = guess + 1

        else:
            print(f"\n🎉 AI Beta Wins in {attempts} attempts!")
            print(f"Secret Number was {secret_number}")
            break

        if low > high:
            print("\nLogic conflict detected. Ending game.")
            break

        time.sleep(2)


if __name__ == "__main__":
    aiVsAi()
