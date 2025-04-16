def main():
    try:
        age = int(input("How old are you? "))
        if age <= 0:
            print("Age cannot be negative or zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        return

    # Define the voting ages for each country
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }

    # Check and display voting eligibility for each country
    for country, min_age in voting_ages.items():
        if age >= min_age:
            print(f"You can vote in {country} where the voting age is {min_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {min_age}.")

if __name__ == '__main__':
    main()
