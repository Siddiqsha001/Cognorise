import random

def roll_dice(sides):
    return random.randint(1, sides)

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    print("Welcome to the Dice Rolling Simulator!")

    sides = get_positive_integer("Enter the number of sides on the dice: ")
    num_rolls = get_positive_integer("Enter the number of rolls: ")

    print(f"\nRolling a {sides}-sided dice {num_rolls} times...\n")

    for roll in range(1, num_rolls + 1):
        result = roll_dice(sides)
        print(f"Roll {roll}: {result}")

    print("\nThanks for using the Dice Rolling Simulator!")

if __name__ == "__main__":
    main()
