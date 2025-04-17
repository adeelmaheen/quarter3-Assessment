def print_multiple(message: str, repeats: int):
    """
    Prints the given message a specified number of times.
    """
    for _ in range(repeats):
        print(message)

def main():
    """
    Main function to prompt user input and display the message multiple times.
    Includes error handling for invalid inputs.
    """
    try:
        message = input("Please type a message: ")
        repeats_input = input("Enter a number of times to repeat your message: ")
        repeats = int(repeats_input)
        if repeats < 0:
            print("Please enter a non-negative integer for repeats.")
            return
        print_multiple(message, repeats)
    except ValueError:
        print("Invalid input. Please enter a valid integer for repeats.")

if __name__ == "__main__":
    main()
