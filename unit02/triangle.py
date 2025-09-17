'''
Program to ask for 3 sides of a triangle and classify it
'''

def main():
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    side3 = float(input("Side 3: "))

    # First check if triangle is possible 
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("The triangle is NOT POSSIBLE")
    # equilateral
    elif side1 == side2 == side3:
        print("The triangle is equilateral")
    # isosceles 
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles")
    # scalene
    else:
        print("The triangle is scalene")


main()