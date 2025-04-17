import random

def guess_my_number():
    # Generate a random number between 0 and 99
    number_to_guess = random.randint(0, 99)

    while True:
        try:
            # Prompt the user for a guess
            user_input = input("Enter a guess between 0 and 99: ").strip()
            
            # Attempt to convert the input to an integer
            guess = int(user_input)

            # Check if the guess is within the valid range
            if not 0 <= guess <= 99:
                print("Please enter a number within the range 0 to 99.")
                continue

            # Compare the guess to the target number
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break  # Exit the loop if the guess is correct

        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Invalid input. Please enter a valid integer between 0 and 99.")

# Entry point of the program
if __name__ == "__main__":
    guess_my_number()
