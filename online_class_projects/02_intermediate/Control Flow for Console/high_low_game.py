# Milestone 1:  Generate the random numbers
import random

def generate_numbers():
    """
    Generates random numbers for the computer and the player.
    Returns:
        tuple: A tuple containing the computer's number and the player's number.
    """
    computer_number = random.randint(1, 100)
    player_number = random.randint(1, 100)
    return computer_number, player_number

def main():
    """
    Main function to execute the High-Low Game's Milestone #1.
    """
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Generate random numbers
    computer_number, player_number = generate_numbers()

    # Display the numbers for testing purposes
    print(f"The computer's number is {computer_number}")
    print(f"Your number is {player_number}")

if __name__ == "__main__":
    main()
