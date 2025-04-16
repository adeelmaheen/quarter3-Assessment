import random

def main():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(10):
        number = random.randint(1, 100)
        print(number, end=' ')
    print()  # Move to the next line after printing all numbers

if __name__ == '__main__':
    main()
