import random
import time

def computerVsComputer():
    start = 1
    end = 100
    total_attempts = 10

    print("\n==============================")
    print("   COMPUTER VS COMPUTER")
    print("==============================")
    print(f"Range: {start} - {end}")
    print(f"Max Attempts: {total_attempts}\n")

    time.sleep(1)

    print("AI Alpha is choosing a secret number...")
    secret_number = random.randint(start, end)
    time.sleep(1)

    print("AI Beta is preparing to guess...\n")
    time.sleep(1)

    attempt = 0

    while attempt < total_attempts:
        attempt += 1
        guess = random.randint(start, end)

        print(f"--- Round {attempt} ---")
        print(f"AI Beta guesses: {guess}")
        time.sleep(1)

        if guess > secret_number:
            print("Result: Too High\n")
        elif guess < secret_number:
            print("Result: Too Low\n")
        else:
            print("\n🎉 AI Beta Wins!")
            print(f"Secret Number: {secret_number}")
            print(f"Attempts Used: {attempt}")
            return

        time.sleep(1)

    print("\n💀 AI Beta Lost!")
    print(f"Secret Number Was: {secret_number}\n")
