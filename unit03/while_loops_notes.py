'''
While Loops Notes

while (condition is true):
    code to run when condition is true

while True:
    code to run (forever)
    if condition to break from the loop

Control-C will kill a program in the terminal
'''
import random

def main():
    # loop to generate random numbers (1-1000) until we get 67
    num = 0
    accumulator = 0
    while num != 67:
        num = random.randrange(1,1001)
        print(num)
        # keep track of how many numbers we've generated
        accumulator += 1
    
    print(f"Numbers generated: {accumulator}")


    # loop until we get heads 5 times in a row 
    current_streak = 0
    total_flips = 0
    while True:
        result = random.choice(["heads","tails"])
        print(result)
        total_flips += 1

        if result == "heads":
            current_streak += 1
        # tails resets the streak
        else:
            current_streak = 0

        # break when there's 5 heads in a row
        if current_streak == 10:
            break
    
    print(total_flips)

main()