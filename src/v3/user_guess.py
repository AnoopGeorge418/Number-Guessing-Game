from src.v3.computer_secret import secret
import sys

def computerVsUser():
    computer_secret = secret(1, 100)
    total_attempts = 5
    current_attempts = 0

    while current_attempts != total_attempts:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess == computer_secret:
                print("Correct - You Win!")
                print('/n')
                break
            elif user_guess > computer_secret:
                print("Try lower")
                current_attempts += 1
                print(f"Total Attempt left: { total_attempts - current_attempts }")
            else:
                print("Try higher")
                current_attempts += 1
                print(f"Total Attempt left: { total_attempts - current_attempts }")

            if current_attempts == 5:
                print(f"GAME OVER, Computer Won! You Lose")
                print(f"The SECRET NUMBER is: {computer_secret} \n")
                break
        
        except ValueError as v:
            print("Please enter valid number.")
        except KeyboardInterrupt as k:
            print(" App Broke....Exiting App")
            sys.exit()

