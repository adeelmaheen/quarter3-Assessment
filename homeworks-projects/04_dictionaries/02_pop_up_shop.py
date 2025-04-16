# Define the fruit prices dictionary
fruit_prices = {
    'apple': 10.0,
    'durian': 25.0,
    'jackfruit': 15.0,
    'kiwi': 12.5,
    'rambutan': 7.0,
    'mango': 8.5
}

def main():
    total_cost = 0.0  # Initialize total cost

    # Iterate over each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        while True:
            try:
                # Prompt user for quantity
                quantity_input = input(f"How many ({fruit}) do you want?: ")
                quantity = int(quantity_input)

                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue

                # Calculate cost and add to total
                total_cost += price * quantity
                break  # Exit the loop if input is valid

            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Display the total cost
    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
