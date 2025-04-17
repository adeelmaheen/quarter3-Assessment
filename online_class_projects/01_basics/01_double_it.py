def main():
    """
    This function prompts the user to enter a number,
    then repeatedly doubles it and prints the result
    until the value reaches 100 or more.
    """
    try:
        # Prompt the user to enter a number
        user_input = input("Enter a number: ")
        curr_value = float(user_input)  # Convert input to a float

        # Check if the entered number is positive
        if curr_value <= 0:
            print("Please enter a positive number greater than zero.")
            return  # Exit the function if the input is not valid

        # Loop to double the number until it reaches 100 or more
        while curr_value < 100:
            curr_value *= 2  # Double the current value
            print(curr_value)  # Print the doubled value

    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
