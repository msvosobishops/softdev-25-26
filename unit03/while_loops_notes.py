'''
While Loops Notes

while (condition is True):
    code to run

while True:
    code to run
    if condition to break from the loop

break is the keyword used to break from a loop 

Control-C is the keyboard shortcut to kill a program in the terminal
'''
import random 

def main():
    # write a loop to generate numbers 1-1000 until we get 10 
    # give num an initial value
    num = 0
    # make a counter variable to keep track of how many numbers we generated 
    counter = 0
    # loop until we get 10
    while num != 10:
        num = random.randrange(1,1001)
        counter += 1
        print(num)
    
    print(f"It took {counter} tries to get 10")

    # write a loop to flip a coin until we get heads 5 times in a row 
    heads_in_a_row = 0
    total_flips = 0

    while True:
        result = random.choice(["heads", "tails"])
        print(result)
        # add to total flips 
        total_flips += 1
        # add to streak
        if result == "heads":
            heads_in_a_row += 1
        # reset streak when you get tails
        else:
            heads_in_a_row = 0
        
        # break when 5 heads in a row
        if heads_in_a_row == 5:
            break

    print(f"It took {total_flips} flips to get heads 5 times")

main()