import madlibs

# madlibs.py

def generate_story():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    story = f"Today I saw a {adjective} {noun} {verb} {adverb} down the street."
    print(story)


# Assuming madlibs.py has a function called generate_story()
madlibs.generate_story()
