def is_odd(number):
    """
    Returns True if the number is odd, False otherwise.
    """
    return number % 2 != 0

def main():
    try:
        user_input = input("Enter an integer: ")
        num = int(user_input)
        if is_odd(num):
            print(f"{num} is an odd number.")
        else:
            print(f"{num} is not an odd number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
