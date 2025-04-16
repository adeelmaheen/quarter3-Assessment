def add_three_copies(my_list, data):
    # Add three copies of 'data' using list multiplication
    my_list.extend([data] * 3)

def main():
    # Get input from the user
    user_input = input("Enter a message to copy: ")

    # Start with an empty list
    messages = []

    # Print list before modification
    print("List before:", messages)

    # Add three copies of the user input to the list
    add_three_copies(messages, user_input)

    # Print list after modification
    print("List after:", messages)

# Call main function when script is run directly
if __name__ == '__main__':
    main()
