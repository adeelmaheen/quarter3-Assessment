
"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
   
    roll_dice()
    roll_dice()
    roll_dice()
   
# to call the main() function.
if __name__ == '__main__':
    main()