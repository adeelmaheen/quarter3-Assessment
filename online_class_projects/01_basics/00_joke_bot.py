import pyjokes  # Importing the pyjokes module to fetch jokes

# Constants
PROMPT = "What do you want? "  # Prompt message for the user
SORRY = "Sorry, I only tell jokes."  # Message for invalid input

def main():
    """
    Main function to prompt user input and display a joke if requested.
    """
    user_input = input(PROMPT).strip()  # Prompting user and removing extra spaces
    if user_input.lower() == "joke":  # Checking if input is 'joke' (case-insensitive)
        print("Here is a joke for you!")
        joke = pyjokes.get_joke(category='neutral')  # Fetching a neutral joke
        print(joke)
    else:
        print(SORRY)  # Informing the user about invalid input

if __name__ == "__main__":
    main()  # Calling the main function
