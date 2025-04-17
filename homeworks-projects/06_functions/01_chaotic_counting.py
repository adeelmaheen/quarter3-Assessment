import random

# Define the likelihood of stopping (e.g., 30% chance)
DONE_LIKELIHOOD = 0.3

def done():
    """
    Returns True with a probability defined by DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """
    Counts from 1 to 10, but may stop early based on the done() function.
    """
    try:
        for i in range(1, 11):
            if done():
                return  # Exit the function early
            print(i, end=' ')
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

if __name__ == "__main__":
    main()
