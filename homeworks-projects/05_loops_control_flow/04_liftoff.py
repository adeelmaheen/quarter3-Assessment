def main():
    """
    Counts down from 10 to 1 and then prints 'Liftoff!'.
    """
    try:
        for i in range(10, 0, -1):
            print(i, end=' ')
        print("Liftoff!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
