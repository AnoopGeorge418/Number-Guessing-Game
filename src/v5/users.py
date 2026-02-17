# enters player 1 name
# enters player 2 name
# chooses which user is the secret holder and who is the guesser
# holder gives hints and messages

from random import shuffle
from src.v5.computer_secret import secret

def userVsUser():
    players = []

    player1 = input("Enter player 1 name: ").title()
    player2 = input('Enter player 2 name: ').title()

    players.append(player1)
    players.append(player2)

    shuffle(players)

    holder = players[0]
    guesser = players[1]

    print(f"{holder} you are the secret holder.")
    print(f"{guesser} you are the guesser.")

    # Holder sets number ONCE
    try:
        start = int(input(f"{holder}, enter starting range: "))
        end = int(input(f"{holder}, enter ending range: "))
        secret_number = int(input(f"{holder}, enter the secret number: "))
    except ValueError:
        print("Invalid number. Restart game.")
        return

    # holder and guesser logic
    total_attempts = 5
    current_attempt = 0

    while current_attempt < total_attempts:
        try:
            # user guess logic
            guess = int(input(f"{guesser}, enter your guess: "))
            current_attempt += 1
            if guess > secret_number:
                print("Try lower")
            elif guess < secret_number:
                print("Try higher")
            else:
                print("Correct! You won! \n")
                return

            print(f"Attempts left: {total_attempts - current_attempt}")

        except ValueError:
            print("Please enter a valid number.")

    print(f"You Lose! The secret number was {secret_number} \n")
        