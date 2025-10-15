'''
Program to check if a number is divisible by 2, 3, both, or neither
'''

def main():
    # get input 
    num = int(input("Give me a number: "))

    # check divisibility 
    # divisible by both
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} is divisible by BOTH 2 and 3")
    # divisible by 2 or 3 individually
    elif num % 2 == 0:
        print(f"{num} is divisible by 2")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3")
    # not divisible by either
    else:
        print(f"{num} is not divisible by either 2 or 3")

main()