import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_valid_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        length = get_valid_length()
        password = generate_password(length)
        print("Generated Password:", password)
        choice = input("Do you want to generate another password? (Yes/No): ").lower()
        if choice != "yes":
            break

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
