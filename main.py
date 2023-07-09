import random

while True:
    user_action = input("Enter a choice (rock, paper or scissors): ")
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
