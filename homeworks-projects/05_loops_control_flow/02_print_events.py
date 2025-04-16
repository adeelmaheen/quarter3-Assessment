def main():
    """
    Prints the first 20 even numbers starting from 0.
    """
    try:
        for i in range(20):
            even_number = i * 2
            print(even_number, end=' ')
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
