import random

def get_user_choice():
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter the number corresponding to your choice: ")

        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "win"
    else:
        return "lose"

def print_choices(user_choice, computer_choice):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

def main():
    print("Welcome to Rock, Paper, Scissors!")

    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\nRound {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nYour score: {user_score}, Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

        round_number += 1

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
