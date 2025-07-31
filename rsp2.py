import random

# Initialize scores
player_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    global player_score, computer_score
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

def display_score():
    print(f"\nCurrent Score - You: {player_score} | Computer: {computer_score}\n")

# Game loop
while True:
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    if player_choice == 'quit':
        break

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Try again.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose {computer_choice}")
    
    determine_winner(player_choice, computer_choice)
    display_score()

print("\nGame Over!")
print(f"Final Score - You: {player_score} | Computer: {computer_score}")
