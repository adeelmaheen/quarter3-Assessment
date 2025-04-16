def tall_enough_extension():
    MIN_HEIGHT = 50  # Minimum height required to ride

    while True:
        user_input = input("How tall are you? (Press Enter without typing anything to quit): ")

        if user_input == "":
            # Exit the loop if the user presses Enter without typing anything
            break

        try:
            height = float(user_input)
        except ValueError:
            print("Please enter a valid number for height.")
            continue

        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    tall_enough_extension()
