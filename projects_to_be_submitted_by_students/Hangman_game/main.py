import random
from words import words
import string

def get_valid_word(words):

    word = random.choice(words) # randomly choose the words from the list
    while "-" in words or " " in words:
