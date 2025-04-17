def greet(name):
    """
    Prints a greeting message to the user.
    """
    print(f"Greetings {name}!")

def main():
    """
    Main function to prompt user input and greet the user.
    Includes error handling for invalid inputs.
    """
    try:
        name = input("What's your name? ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        greet(name)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
