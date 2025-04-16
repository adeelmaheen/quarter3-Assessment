def main():
    # Initialize an empty dictionary to store number counts
    counts = {}

    while True:
        try:
            # Prompt the user to enter a number
            user_input = input("Enter a number (or press Enter to finish): ")

            # If the input is empty, exit the loop
            if not user_input:
                break

            # Convert the input to an integer
            num = int(user_input)

            # Update the count for the entered number
            # If the number is not in the dictionary, get() returns 0
            counts[num] = counts.get(num, 0) + 1

        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Please enter a valid integer.")

    # After collecting inputs, display the counts
    for num, count in counts.items():
        # Determine the correct pluralization for "time"
        time_word = "times" if count > 1 else "time"
        print(f"{num} appears {count} {time_word}.")

# Entry point of the program
if __name__ == "__main__":
    main()
