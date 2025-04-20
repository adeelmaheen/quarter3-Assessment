import random
from words import words
import string

def get_valid_word(words):

    word = random.choice(words) # randomly choose the words from the list
    while "-" in words or " " in words:
        word = random.choice(words)
    
    return word # return the word to be guessed

def hangman():
    word = get_valid_word(words) # get the word to be guessed
    word_letters = set(word) # letters in the word to be guessed
    alphabet = set(string.ascii_uppercase) # all letters in the alphabet
    used_letters = set() # letters that have been guessed

    lives = 6 # number of lives

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word] # list of letters in the word to be guessed
        print("Current word: ", " ".join(word_list)) # print the current word

        user_letter = input("Guess a letter: ").upper() # get the letter from the user

        if user_letter in used_letters:
            print("You have already guessed that letter. Please try again.")
        elif user_letter in alphabet:
            used_letters.add(user_letter) # add the letter to the list of used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter) # remove the letter from the list of letters in the word to be guessed
            else:
                lives -= 1 # reduce the number of lives by 1
                print("Letter is not in the word.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

print("Welcome to Hangman!")
hangman() # call the hangman function to start the game