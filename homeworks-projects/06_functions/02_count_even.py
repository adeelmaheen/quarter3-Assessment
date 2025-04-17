def count_even():
    """
    Prompts the user to enter integers until an empty input is received.
    Counts and prints the number of even numbers entered.
    """
    numbers = []
    while True:
        try:
            user_input = input("Enter an integer or press enter to stop: ")
            if user_input == "":
                break
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    even_count = sum(1 for num in numbers if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

if __name__ == "__main__":
    count_even()
