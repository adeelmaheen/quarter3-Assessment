def main():
    try:
        year = int(input("Enter a year: "))
        if year < 0:
            print("Please enter a valid positive year.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        return

    # Leap year conditions:
    # 1. If the year is divisible by 4 and not divisible by 100, it's a leap year.
    # 2. If the year is divisible by 400, it's a leap year.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()
