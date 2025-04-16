def main():
    # Initialize an empty dictionary to store contacts
    phonebook = {}

    while True:
        # Display the menu options
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Look Up Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        # Prompt the user to choose an option
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Add a new contact
            name = input("Enter contact name: ").strip()
            number = input("Enter phone number: ").strip()
            if name in phonebook:
                print(f"{name} already exists in the phonebook.")
            else:
                phonebook[name] = number
                print(f"Contact '{name}' added successfully.")

        elif choice == '2':
            # Look up an existing contact
            name = input("Enter contact name to look up: ").strip()
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}.")
            else:
                print(f"Contact '{name}' not found in the phonebook.")

        elif choice == '3':
            # Delete an existing contact
            name = input("Enter contact name to delete: ").strip()
            if name in phonebook:
                del phonebook[name]
                print(f"Contact '{name}' deleted successfully.")
            else:
                print(f"Contact '{name}' not found in the phonebook.")

        elif choice == '4':
            # Display all contacts
            if phonebook:
                print("\nAll Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("The phonebook is currently empty.")

        elif choice == '5':
            # Exit the program
            print("Exiting the phonebook. Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
