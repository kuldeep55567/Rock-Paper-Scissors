import random
def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Welcome to the Rock-Paper-Scissors game!")
    print("Please choose one: rock, paper, or scissors.")
    player_choice = input("Your choice: ").lower()

    if player_choice in choices:
        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)
        print(winner(player_choice, computer_choice))
    else:
        print("Invalid choice. Please try again.")

play_game()