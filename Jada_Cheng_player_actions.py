#player_actions.py

Yes = "Y"
No = "N"

def check_play_again(user_input):
    if user_input == Yes:
        print("Let's play again!")
    elif user_input == No:
        print("See you next time!")
    else:
        print("Invalid input")

check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
