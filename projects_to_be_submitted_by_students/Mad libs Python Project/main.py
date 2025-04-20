# string concatenation ( how to put string together)
# suppose we want to create a string that say's "subscribe to ______"

youtuber = "Maheen "   # some string variale

def main():

    #  a few ways to do this 
    print("Subscribe to " + youtuber)
    print("Subscribe to {}".format(youtuber))
    print(f"Subscribe to {youtuber}")



if __name__ == "__main__":
    main()