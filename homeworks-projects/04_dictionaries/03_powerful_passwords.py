import hashlib

def hash_password(password):
    """
    Hashes a password using SHA-256 and returns the hexadecimal digest.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Verifies if the provided password matches the stored hashed password for the given email.

    Parameters:
    - email (str): The user's email address.
    - password_to_check (str): The password entered by the user.
    - stored_logins (dict): A dictionary mapping emails to their hashed passwords.

    Returns:
    - bool: True if the password is correct, False otherwise.
    """
    # Retrieve the stored hash for the given email
    stored_hash = stored_logins.get(email)
    if stored_hash is None:
        # Email not found in stored_logins
        return False

    # Hash the provided password
    hashed_input = hash_password(password_to_check)

    # Compare the hashed input with the stored hash
    return hashed_input == stored_hash

def main():
    # Predefined stored logins with hashed passwords
    stored_logins = {
        'user@example.com': hash_password('securepassword123'),
        'admin@example.com': hash_password('adminpass456')
    }

    # User input
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Attempt login
    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == "__main__":
    main()
