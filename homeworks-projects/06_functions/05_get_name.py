import random

def get_random_name():
    """
    Returns a randomly selected name from the list.
    """
    names = ["Sophia", "Momina", "Ibrahim", "Noah"]
    return random.choice(names)

def main():
    try:
        name = get_random_name()
        print(f"Howdy {name}! 🤠")
    except IndexError:
        print("The list of names is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
