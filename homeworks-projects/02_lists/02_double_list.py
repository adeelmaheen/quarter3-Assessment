"""
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]
"""

def main():
#     # Sample list of numbers
#     num_list = [1, 2, 3, 4]
#     print(f"List of numbers to be doubled: {num_list}")

#     # Double each number in the list
#     doubled_list = [number * 2 for number in num_list]

#     # Display the result
#     print(f"The doubled numbers are: {doubled_list}")

    list_of_numbers = [1, 2, 3, 4]
    print(f"List of number to be doubled: {list_of_numbers}")

    for i in range(len(list_of_numbers)):
        number_of_index = list_of_numbers[i]
        list_of_numbers[i] = number_of_index * 2
    print(f"The doubled numbers are: {list_of_numbers}")

    
if __name__ == '__main__':
    main()