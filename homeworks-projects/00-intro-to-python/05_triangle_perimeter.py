def main():
    # Prompting the user to enter the lengths of the sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Calculating the perimeter
    perimeter = side1 + side2 + side3
    
    # ANSI escape codes for italics and color (green)
    print(f"\033[3m\033[32mThe perimeter of the triangle is {perimeter}\033[0m")



# Python file to call the main() function.
if __name__ == '__main__':
    main()
