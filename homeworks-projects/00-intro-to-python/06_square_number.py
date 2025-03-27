def main():
    # Asking the user to input a number
    number = float(input("Type a number to see its square: "))
    
    # Calculating the square of the number
    square = number ** 2
    
    # Printing the result with colored output
    print(f"{number} squared is {square}")


# Python file to call the main() function.
if __name__ == '__main__':
    main()
