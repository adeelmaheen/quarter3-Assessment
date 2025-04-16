MAX_LENGTH = 3  # You can adjust this value for testing purposes

def shorten(lst):
    # Continue removing elements from the end until the list length is MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Removes and returns the last item
        print("Removed:", removed_item)
        
def main():
    # Prompt the user for the number of items
    num_items = int(input("How many items will you enter? "))

    # Initialize an empty list
    user_list = []

    # Collect items from the user
    for i in range(num_items):
        item = input(f"Enter item #{i + 1}: ")
        user_list.append(item)

    # Display the original list
    print("Original list:", user_list)

    # Call the shorten function
    shorten(user_list)

    # Display the shortened list
    print("Shortened list:", user_list)

# Ensure the main function runs when the script is executed
if __name__ == '__main__':
    main()
