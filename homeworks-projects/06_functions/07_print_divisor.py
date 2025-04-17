def print_divisors(num: int):
    """
    Prints all divisors of the given number.
    """
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

def main():
    """
    Main function to prompt user input and display divisors.
    Includes error handling for invalid inputs.
    """
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Please enter a positive integer.")
            return
        print_divisors(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
