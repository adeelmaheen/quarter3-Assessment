import random

def computer_guesses():
    """
    The computer attempts to guess the number the user is thinking of.
    """
    print("\nThink of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 5

    while attempts > 0 and low <= high:
        guess = random.randint(low, high)
        print(f"\nIs your number {guess}?")
        feedback = input("Enter 'h' if too high, 'l' if too low, 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"🎉 Yay! I guessed your number in {6 - attempts} attempt(s)!")
            return
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
            continue

        attempts -= 1

    print("\n😞 I couldn't guess your number within the given attempts.")

def main():
    """
    Main function to control the game flow.
    """
    while True:
        computer_guesses()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ('yes', 'y'):
            print("Thank you for playing! Goodbye.")
            break

# Entry point of the program
if __name__ == "__main__":
    main()
