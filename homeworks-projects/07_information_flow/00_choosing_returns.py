# Define the legal adult age
ADULT_AGE = 18

def is_adult(age):
    """
    Returns True if the age is greater than or equal to ADULT_AGE, otherwise False.
    """
    return age >= ADULT_AGE

def main():
    """
    Main function to prompt user input and check if the person is an adult.
    Includes error handling for invalid inputs.
    """
    try:
        age = int(input("How old is this person?: "))
        print(is_adult(age))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
