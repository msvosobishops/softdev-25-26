'''
Count up hex digits in a string
'''

def main():
    number_string = input("Enter a string: ")
    total = 0

    for digit in number_string:
        if digit == "a":
            total += 10
        elif digit == "b":
            total += 11
        elif digit == "c":
            total += 12
        elif digit == "d":
            total += 13
        elif digit == "e":
            total += 14
        elif digit == "f":
            total += 15
        # if digit isn't a letter then it must be a number
        else:
            total += int(digit)

    print(total)


main()