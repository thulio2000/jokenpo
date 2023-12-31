import random
from enum import IntEnum

class Action(IntEnum): # Player options
    Rock = 0
    Paper = 1
    Scissors = 2


def get_user_selection(): # Human player choice
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection(): #computer action
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


"""Next step is the determine winner function"""

def determine_winner(user_action, computer_action):
    """ Determines outcome of the games, wins, losses and ties """
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes Scissors! You win.")
        else:
            print("Paper covers Rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers Rock! You lose.")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")


while True:
    """ Game logic, tests whether player choice is valid, determines winner and gives option to play again """
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
