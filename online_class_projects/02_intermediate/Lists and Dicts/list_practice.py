# This code defines a list of fruits, appends "mango" to the list, and prints the updated list.
def main():
    print("++++++++++++++++++++++++++++++++++  List Practice ++++++++++++++++++++++++++++ ", end="\n\n")
    fruit_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "pineapple", "kiwi", "lemon"]
    # Print the original list
    print(fruit_list)
    # Print the length of the list
    print("Length of the list:", len(fruit_list))
    # Append "mango" to the list
    fruit_list.append("mango")
    # Print the updated list
    print("After appending mango:")
    print(fruit_list)
    # Print the length of the updated list
    print("Length of the updated list:", len(fruit_list))


if __name__ == "__main__":
    main()
