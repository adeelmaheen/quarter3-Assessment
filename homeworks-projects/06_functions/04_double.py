def double(num):
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)
        result = double(num)
        print(f"Double that is {result}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
