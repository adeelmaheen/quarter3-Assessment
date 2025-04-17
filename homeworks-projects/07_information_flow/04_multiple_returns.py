# A memory-efficient and error-handled Python program to collect user data
def get_user_data():
    """
    Prompts the user for first name, last name, and email,
    and returns them as a tuple.
    Includes error handling for empty inputs.
    """
    try:
        first_name = input("What is your first name?: ").strip()
        if not first_name:
            raise ValueError("First name cannot be empty.")

        last_name = input("What is your last name?: ").strip()
        if not last_name:
            raise ValueError("Last name cannot be empty.")

        email = input("What is your email address?: ").strip()
        if not email or "@" not in email or "." not in email:
            raise ValueError("Please enter a valid email address.")

        return first_name, last_name, email

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None  # Return None if input was invalid

def main():
    user_data = get_user_data()
    if user_data:
        print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
