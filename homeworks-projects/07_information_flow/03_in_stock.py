# Sophia's fruit inventory
inventory = {
    'apple': 10,
    'banana': 5,
    'pear': 1000,
    'orange': 0
}

def num_in_stock(fruit):
    """
    Returns the number of the specified fruit in stock.
    If the fruit is not in the inventory, returns 0.
    """
    try:
        return inventory[fruit.lower()]
    except KeyError:
        return 0

def main():
    """
    Main function to prompt user input and display stock information.
    Includes error handling for invalid inputs.
    """
    try:
        fruit = input("Enter a fruit: ").strip().lower()
        if not fruit:
            raise ValueError("Input cannot be empty.")
        stock = num_in_stock(fruit)
        if stock > 0:
            print("This fruit is in stock! Here is how many:")
            print(stock)
        else:
            print("This fruit is not in stock.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
