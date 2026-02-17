import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}


def ask_ai(prompt):
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    data = response.json()

    # If model is loading
    if isinstance(data, dict) and "error" in data:
        print("Model waking up... waiting 20 seconds")
        time.sleep(20)
        return ask_ai(prompt)

    try:
        return data[0]["generated_text"]
    except:
        return "50"


def aiVsUser():
    print("\n===== AI VS USER (HuggingFace) =====\n")
    print("Think of a number between 1 and 100.")
    print("Answer honestly!\n")

    low = 1
    high = 100
    attempts = 0

    context = "Guess a number between 1 and 100."

    while True:
        attempts += 1

        prompt = f"""
        You are guessing a number.
        Range is {low} to {high}.
        Suggest ONE number only.
        Previous context: {context}
        """

        ai_response = ask_ai(prompt)

        # extract number from text
        guess = ''.join(filter(str.isdigit, ai_response))
        if guess == "":
            guess = str((low + high) // 2)

        guess = int(guess)

        print(f"\nAI guesses: {guess}")

        feedback = input("Higher (h) / Lower (l) / Correct (c): ").lower()

        if feedback == 'c':
            print(f"\n🎉 AI won in {attempts} attempts!")
            break

        elif feedback == 'h':
            low = guess + 1
            context = "Number is higher."

        elif feedback == 'l':
            high = guess - 1
            context = "Number is lower."

        else:
            print("Invalid input. Use h/l/c")

        if low > high:
            print("\nSomething is wrong. Are you cheating? 😄")
            break


if __name__ == "__main__":
    aiVsUser()
