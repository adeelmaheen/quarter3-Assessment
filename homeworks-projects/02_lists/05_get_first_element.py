def get_first_element(lst):
    # Print the first element in the list
    print("First element:", lst[0])

def main():
    # Ask the user how many items they want to input
    num_items = int(input("How many items will you enter? "))

    # Initialize an empty list
    user_list = []

    # Collect list elements from the user
    for i in range(num_items):
        item = input(f"Enter item #{i + 1}: ")
        user_list.append(item)

    # Call the function to print the first element
    get_first_element(user_list)

# This line ensures main() runs when the script is executed
if __name__ == '__main__':
    main()
