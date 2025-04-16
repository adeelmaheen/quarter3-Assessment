import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            # Prompt the user to enter a guess
            guess = int(input("Enter a guess: "))
            
            # Compare the guess to the secret number and provide feedback
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  # Exit the loop if the guess is correct
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
