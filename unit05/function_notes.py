'''
Function Notes
11/21/25

All docstrings need purpose, parameters, and returns
'''
import random
import time

def print_random_num():
    '''prints random number from 1-100, no parameters or returns'''
    num = random.randrange(1, 101)
    print(num)

def countdown():
    '''countdown from 3 to 1 waiting 1 second between, no parameters or returns'''
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

def greet_user(name: str):
    '''Counts down and then greets the user by name, takes in name (str), no returns'''
    countdown()
    print(f"Welcome, {name}!")
    print("Happy Thanksgiving!")

def calculate_area(length: float, width: float) -> float:
    '''calculates area of rectangle 
        takes in the length and width, returns the area 
    '''
    area = length * width
    return area

def main():
    # for i in range(5):
    #     print_random_num()
    # countdown()

    # user = input("Enter your name: ")
    # greet_user(user)

    area = calculate_area(10, 8)
    print(f"The area is {area}")




main()