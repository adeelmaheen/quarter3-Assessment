def main():
    # Prompt the user for the number of even numbers to print
    try:
        count = int(input("How many even numbers would you like to print? "))
        if count < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Generate and print the specified number of even numbers
    for i in range(count):
        print(i * 2, end=' ')

if __name__ == '__main__':
    main()
