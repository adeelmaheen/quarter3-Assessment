def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers by iterating through each element.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The sum of the numbers in the list.
    """
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    # Sample list of numbers
    num_list = [8, 2, 3, 0, 7]
    print(f"List of numbers to be sum: {num_list}")
    # Calculate the sum
    result = calculate_sum(num_list)

    # Display the result
    print(f"The sum of the numbers is: {result}")

if __name__ == '__main__':
    main()