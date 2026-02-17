import time, sys
from src.v4.user_guess import computerVsUser
from src.v4.users import userVsUser
from src.v4.computers import computerVsComputer
from src.v4.online import onlinePlay
from src.v4.aiVsUser import aiVsUser
from src.v4.ais import aiVsAi

def startGame():
    print("Welcome to Number Guessing Game Application Version 4.")
    time.sleep(1)

    while True:
        print('Please choose the mode of game to play Number Guessing Game.')
        print('1. Default - Computer vs User')
        print('2. User vs User')
        print('3. Computer vs Computer')
        print('4. Play Online')
        print('5. Ai vs User')
        print('6. Ai vs Ai')
        print('7. Exit from the game')

        try: 
            print('\n')
            user_choice = int(input('Enter your Choice from above numbers: '))
            if user_choice == 1:
                computerVsUser()
            elif user_choice == 2:
                userVsUser()
            elif user_choice == 3:
                computerVsComputer()
            elif user_choice == 4:
                onlinePlay()
            elif user_choice == 5:
                aiVsUser()
            elif user_choice == 6:
                aiVsAi()
            elif user_choice == 7:
                print('Exiting from Application. Play Us Again!')
                sys.exit()
            

        except ValueError as v:
            print(f'Please enter a number from above: {v}')
            print('\n')
        except KeyboardInterrupt as k:
            print(f' Forcefully Exiting from Application: {k}')
            sys.exit()

