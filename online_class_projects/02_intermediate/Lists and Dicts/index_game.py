# Function to access an element by index
def access_element(lst, index):
    """
    Returns the element at the specified index if it exists.
    Otherwise, returns an error message.
    """
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range."

# Function to modify an element at a specific index
def modify_element(lst, index, new_value):
    """
    Replaces the element at the specified index with new_value.
    Returns a success message or an error message if the index is invalid.
    """
    try:
        lst[index] = new_value
        return f"Element at index {index} updated to {new_value}."
    except IndexError:
        return f"Error: Index {index} is out of range."

# Function to slice the list from start_index to end_index (exclusive)
def slice_list(lst, start_index, end_index):
    """
    Returns a sublist from start_index to end_index.
    Handles cases where indices are out of range.
    """
    # Adjust indices if they are out of bounds
    start_index = max(start_index, 0)
    end_index = min(end_index, len(lst))
    if start_index >= end_index:
        return []
    return lst[start_index:end_index]

# Main function to run the Index Game
def main():
    """
    Main function to run the Index Game.
    Allows the user to access, modify, or slice the list.
    """
    # Initialize a list with mixed data types
    data = [10, "Python", 3.14, "AI", True]

    while True:
        print("\nCurrent List:", data)
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            try:
                idx = int(input("Enter the index to access: "))
                result = access_element(data, idx)
                print("Result:", result)
            except ValueError:
                print("Error: Please enter a valid integer index.")
        elif choice == '2':
            try:
                idx = int(input("Enter the index to modify: "))
                new_val = input("Enter the new value: ")
                result = modify_element(data, idx, new_val)
                print(result)
            except ValueError:
                print("Error: Please enter a valid integer index.")
        elif choice == '3':
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(data, start, end)
                print("Sliced List:", result)
            except ValueError:
                print("Error: Please enter valid integer indices.")
        elif choice == '4':
            print("Exiting the Index Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Entry point of the program
if __name__ == "__main__":
    main()
