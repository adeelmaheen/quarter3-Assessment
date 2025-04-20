# string concatenation ( how to put string together)
# suppose we want to create a string that say's "subscribe to ______"

youtuber = "Maheen "   # some string variale

def main():

    #  a few ways to do this 
    print("Subscribe to " + youtuber)
    print("Subscribe to {}".format(youtuber))
    print(f"Subscribe to {youtuber}")

    adjective = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    noun = input("Noun: ")
    favorite_person = input("Favorite person: ")
    
    matlib = f"Computer programming is so {adjective} and fun! It makes me so excited all the time because \
    I love to {verb1}.Stay hyderated and {verb2} like you are {noun} and I love {favorite_person}."

    print(matlib)
    
if __name__ == "__main__":
    main()