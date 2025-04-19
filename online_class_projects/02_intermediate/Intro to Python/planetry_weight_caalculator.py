def main():
    # Define gravity ratios for each planet (as a percentage of Earth's gravity)
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Ask the user for their weight on Earth
    try:
        earth_weight = float(input("Enter a weight on Earth: "))
    except ValueError:
        print("Please enter a valid number for weight.")
        return

    # Ask the user to select a planet
    planet_name = input("Enter a planet (e.g. Mars, Jupiter, Venus): ").title()

    # Check if the planet is in our dictionary
    if planet_name in planet_gravity:
        # Calculate weight on the chosen planet
        gravity_ratio = planet_gravity[planet_name]
        planet_weight = earth_weight * gravity_ratio
        rounded_weight = round(planet_weight, 2)

        # Display the result
        print(f"The equivalent weight on {planet_name}: {rounded_weight}")
    else:
        # Handle invalid planet input
        print("Invalid planet name. Please enter a valid planet from the solar system.")

# Only run the main function if this file is executed directly
if __name__ == "__main__":
    main()











