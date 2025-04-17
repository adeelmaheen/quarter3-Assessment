def main():
    """
    Performs a countdown from 10 to 1 and then prints 'Liftoff!'.
    """
    for i in range(10, 0, -1):
        print(i, end=' ')
    print("Liftoff!")

if __name__ == "__main__":
    main()
