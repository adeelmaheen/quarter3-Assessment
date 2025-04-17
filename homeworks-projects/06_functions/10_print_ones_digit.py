def print_ones_digit(num):
    """
    Prints the ones digit of the given integer.
    """
    ones_digit = abs(num) % 10
    print(f"The ones digit is {ones_digit}")

def main():
    """
    Main function to prompt user input and display the ones digit.
    Includes error handling for invalid inputs.
    """
    try:
        num = int(input("Enter a number: "))
        print_ones_digit(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
