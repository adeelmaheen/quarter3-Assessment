def main():
    """
    Prompts the user to enter a number, then repeatedly doubles it and prints the result
    until the value reaches or exceeds 100.
    """
    try:
        curr_value = float(input("Enter a number: "))
        while curr_value < 100:
            curr_value *= 2
            print(curr_value)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
