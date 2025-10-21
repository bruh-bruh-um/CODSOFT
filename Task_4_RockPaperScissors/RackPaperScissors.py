import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "User"
    else:
        return "Computer"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()
        if user_choice == 'quit':
            print("\nThanks for playing!")
            print(f"Final Score - You: {user_score} | Computer: {computer_score}")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "User":
            print(" You win this round!")
            user_score += 1
        elif winner == "Computer":
            print(" Computer wins this round!")
            computer_score += 1
        else:
            print(" It's a tie!")

        print(f"Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
