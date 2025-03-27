"""
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


"""

def main():
    foot :int = 1
    inch : int = 12 

    print("\t\t\t\t Feet Conversion into inches ⚖ \t\t")

    feet = int(input("Enter you feet to convert in inches: "))

    convert = feet * inch

    print(f"You are {convert} Inches tall. 😎")

if __name__ == '__main__':
    main()
