def main():
    # Initialize an empty list to store user inputs
    user_list = []

    while True:
        # Prompt the user for input
        value = input("Enter a value: ")

        # Check if the input is an empty string
        if value == "":
            # If empty, break the loop
            break
        else:
            # Otherwise, add the input to the list
            user_list.append(value)

    # Print the final list of entered values
    print("Here's the list:", user_list)

# This ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
