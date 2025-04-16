def main():
    """
    Prompts the user to type a specific affirmation until they do so correctly.
    """
    affirmation = "I am capable of doing anything I put my mind to."
    prompt = f"Please type the following affirmation:\n{affirmation}\n"

    try:
        while True:
            user_input = input(prompt)
            if user_input == affirmation:
                print("That's right! :)")
                break
            else:
                
                print("Hmmm That was not the affirmation.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
