"""
Simulate rolling two dice, and prints results of each roll as well as the total.

"""
import random

dice_sides : int = 6

def main():
    dice1 = random.randint(1,dice_sides)
    dice2 = random.randint(1,dice_sides)

    total = dice1 + dice2 

    print(f"Dice have, {dice_sides} sides!")
    print(f"First die is: {dice1}")
    print(f"Second die is: {dice2}")
    print(f"the total of two dies is {total}")

if __name__ == '__main__':
    main()