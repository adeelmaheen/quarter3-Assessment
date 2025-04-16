def get_last_element(lst):
    # Print the last element in the list using negative indexing
    print("Last element:", lst[-1])

def main():
    # Ask how many items the user wants to enter
    num_items = int(input("How many items will you enter? "))

    # Initialize an empty list
    user_list = []

    # Get items from the user
    for i in range(num_items):
        item = input(f"Enter item #{i + 1}: ")
        user_list.append(item)

    # Call the function to print the last element
    get_last_element(user_list)

# Run the main function
if __name__ == '__main__':
    main()
