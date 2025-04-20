import random

def play_game():
    """
    Runs a single round of the Guess the Number game.
    """
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 5  # Total attempts allowed

    print("\nWelcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it correctly.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skip to the next iteration

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number in {attempt} attempt(s).")
            break  # Exit the loop if guessed correctly
        elif guess < number_to_guess:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    else:
        # This block executes if the loop wasn't broken out of (i.e., user didn't guess correctly)
        print(f"\n😞 You've used all {attempts} attempts. The number was {number_to_guess}.")

def main():
    """
    Main function to control the game flow.
    """
    while True:
        play_game()  # Play a round of the game
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ('yes', 'y'):
            print("Thank you for playing! Goodbye.")
            break  # Exit the loop and end the game

# Entry point of the program
if __name__ == "__main__":
    main()
