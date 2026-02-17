from src.v1.computer_secret import secret
import sys

def user():
    computer_secret = secret()

    while True:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess == computer_secret:
                print("Correct - You Win!")
                break
            elif user_guess > computer_secret:
                print("Try lower")
            else:
                print("Try higher")
        
        except ValueError as v:
            print("Please enter valid number.")
        except KeyboardInterrupt as k:
            print(" App Broke....Exiting App")
            sys.exit()
