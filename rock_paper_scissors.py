import random

user_wins = 0
computer_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It's a tie!")
        ties += 1
    elif (
        (user_input == "rock" and computer_pick == "scissors")
        or (user_input == "paper" and computer_pick == "rock")
        or (user_input == "scissors" and computer_pick == "paper")
    ):
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

print(f"You won: {user_wins}.")
print(f"Computer won: {computer_wins}.")
print(f"Ties: {ties}.")
print("Thanks for playing!")
