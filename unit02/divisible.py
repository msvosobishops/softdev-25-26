'''
Check if a number is divisible by 2, 3, both, or neither
'''

def main():
    # get number
    num = int(input("Number: "))

    # if divisible by 2 and 3
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3")
    # divisible by 2 or 3 individually
    elif num % 2 == 0:
        print(f"{num} is divisible by 2")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3")
    # otherwise its not divisible by 2 or 3
    else:
        print(f"{num} is NOT divisible by 2 or 3")

main()