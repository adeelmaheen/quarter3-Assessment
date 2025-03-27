def main():
    # Asking the user for their favorite animal
    favorite_animal = input("What's your favorite animal? ")

    # Responding with a message including the user's favorite animal in bold
    print(f"\033[1mMy favorite animal is also {favorite_animal}!\033[0m")


# Python file to call the main() function.
if __name__ == '__main__':
    main()
