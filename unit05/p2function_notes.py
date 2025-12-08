'''
Function notes 
11/20/25
'''
import random 
import time

def print_random_number():
    '''
    Purpose: print random number between 1-100 
    Parameters: none
    Returns: none
    '''
    print(random.randrange(1,101))


def get_random_number(a: int, b: int):
    '''
    Purpose: get random number between a to b (inclusive)
    Parameters: none
    Returns: random int a to b
    '''
    my_number = random.randrange(a, b + 1)
    return my_number


def countdown():
    '''counts down from 3 to 1, no parameters or returns'''
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)


def greet_user(name: str):
    '''greets a user with a countdown, takes in name, no returns'''
    print(f"Welcome {name}!")
    countdown()
    print("Goodbye")


def main():
    # countdown()
    # print("Here's your random number:")
    # print_random_number()

    # greet_user("Benny")

    # username = input("What is your name? ")
    # greet_user(username)

    # save the random number 
    my_number = get_random_number(20, 30)
    print(my_number)

main()