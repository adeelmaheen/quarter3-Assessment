import random

def generate_random_numbers():
    """
    Generates and prints 10 random integers between 1 and 100.
    """
    for _ in range(10):
        print(random.randint(1, 100), end=' ')
    print()  # For a newline after printing the numbers

if __name__ == "__main__":
    generate_random_numbers()
