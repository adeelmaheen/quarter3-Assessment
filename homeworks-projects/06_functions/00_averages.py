def calculate_average(num1, num2):
    """
    Calculates the average of two numbers.
    """
    return (num1 + num2) / 2

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        average = calculate_average(num1, num2)
        print(f"The average of {num1} and {num2} is: {average}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
