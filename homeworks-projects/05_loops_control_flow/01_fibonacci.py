def main():
    """
    Prints the Fibonacci sequence up to a maximum value.
    """
    MAX_VALUE = 10000  # Constant representing the maximum value
    a, b = 0, 1  # Initialize the first two Fibonacci numbers

    print("Fibonacci sequence up to", MAX_VALUE, ":")
    try:
        while a < MAX_VALUE:
            print(a, end=' ')
            a, b = b, a + b  # Update to the next Fibonacci number
    except Exception as e:
        print("\nAn error occurred:", e)

if __name__ == "__main__":
    main()
