'''
Get 3 numbers and print out the max among them
'''

def main():
    # get 3 numbers
    a = float(input("First number: "))
    b = float(input("Second number: "))
    c = float(input("Third number: "))

    # compare them and print out the largest
    # a is the largest (or they're all equal)
    if a >= b and a >= c:
        print(f"{a} is the largest")
    # b is the largest
    elif b >= a and b >= c:
        print(f"{b} is the largest")
    # c is the largest
    else:
        print(f"{c} is the largest")

main()