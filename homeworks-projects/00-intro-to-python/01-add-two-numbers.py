def main():
    print("Welcome to the Sum Calculator!")
    
    # Prompting the user to enter the first number
    try:
        num1 = int(input("Please enter the first number: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return
    
    # Prompting the user to enter the second number
    try:
        num2 = int(input("Please enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return
    
    # Calculating the sum
    total_sum = num1 + num2
    
    # Displaying the result
    print(f"The sum of {num1} and {num2} is: {total_sum}")


# This provided line is required at the end
# Python file to call the main() function.
if __name__ == '__main__':
    main()
