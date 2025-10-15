'''
Create a rectangle of numbers 
'''
import time

def main():
    rows = int(input("How many rows? "))
    cols = int(input("How many columns? "))

    # Option 1: Nested Loops

    # loop to make many rows
    for j in range(rows):
        # make one row 
        for i in range(cols):
            print(j+1, end=" ")
            time.sleep(0.5)
        print()

    print("Option 2")
    # Option 2: no nested loops 
    for j in range(1, rows+1):
        print(f"{j} " * cols)


main()