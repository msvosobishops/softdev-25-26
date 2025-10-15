'''
For loops with range notes

for i in range(#)
i will be a number, starting from 0 and going up to but not including #
'''

import random

def main():
    # example loop
    # for i in range(8):
    #     print(i)

    # Write a for loop to print the first 10 even numbers (2, 4, 6,..., 20)
    for i in range(21):
        # only even and non-zero numbers to print
        if i % 2 == 0 and i != 0:
            print(i)

    # Another option
    for i in range(10):
        print(2*i + 2)

    # Write a for loop to print the first 11 perfect squares (0, 1, 4,..., 100)
    for i in range(11):
        print(i * i)

    # Write a for loop that gets 3 numbers from the user and adds each of them 
    # to the total. At the end, print the total 
    total = 0
    for i in range(3):
        add = int(input("Enter a number: "))
        total += add
    print(total)

    # Print the numbers 0-9 on one line separated by commas
    for i in range(10):
        print(i, end=", ")
    print()

    # Flip a coin 5 times
    for i in range(5):
        coin = ["heads", "tails"]
        result = random.choice(coin)
        print(result)
    
    # roll die
    for i in range(5):
        result = random.randrange(1,7)
        print(result)
    

main()