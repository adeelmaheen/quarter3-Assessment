import secrets
import string

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def generate_password(length, charset):
    return ''.join(secrets.choice(charset) for _ in range(length))

def main():
    print("\n\tWelcome to Your Secure Password Generator\n")

    # Define character set
    charset = string.ascii_letters + string.digits + string.punctuation

    # Get user inputs with validation
    num_passwords = get_positive_int("Enter the number of passwords to generate: ")
    password_length = get_positive_int("Enter the desired password length: ")

    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(password_length, charset)
        print(f"{i + 1}: {password}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
