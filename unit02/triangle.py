'''
Get three sides from a user and classify the triangle by sides
'''

def main():
    # get inputs
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    side3 = float(input("Side 3: "))

    # check if triangle is not possible
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        print("Triangle is not possible")
    # equilateral 
    elif side1 == side2 == side3:
        print("Equilateral")
    # isosceles
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles")
    # scalene
    else:
        print("Scalene")

main()