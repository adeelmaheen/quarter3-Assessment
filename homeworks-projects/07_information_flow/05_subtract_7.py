def subtract_seven(num):
    """
    Subtracts 7 from the provided number.

    Parameters:
    num (int): The number from which to subtract 7.

    Returns:
    int: The result after subtraction.
    """
    return num - 7

def main():
    """
    Main function to execute the subtraction operation.
    Prompts the user for input and displays the result.
    Includes error handling for invalid inputs.
    """
    try:
        user_input = input("Enter a number: ")
        num = int(user_input)
        result = subtract_seven(num)
        print(f"{num} minus 7 is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
