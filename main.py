import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(Selection)
    return action

"""Next step is the determine winner function"""
while True:
    #user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
    user_action = int(user_input)
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}. \n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a draw.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lost!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissor cuts paper! You lost!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You win!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
