'''
Functions with return values

When you define your function, specify return data type using ->
If a function doesn't return anything, it returns None
'''
import random

def can_vote(age: int) -> bool:
    '''takes in age and returns True if they can vote or False otherwise'''
    if age >= 18:
        return True 
    else:
        return False 


def get_rps() -> str:
    '''returns random string of rock/paper/scissors. no parameters'''
    pick = random.choice(['rock', 'paper', 'scissors'])
    return pick 


def add_student(name, age=14, gpa=4.0, computer="Mac", gender="n/a"):
    '''adds a student to our roster'''
    print(f"Welcome to Software Development, {name}!")
    print(f"age: {age}, gpa: {gpa}, computer: {computer}, gender: {gender}")
    if gpa < 2.5:
        print("You need to come to office hours to improve your grade")

def add_apple_to_list(lst: list):
    '''appends apple to a list, returns None'''
    new_lst = lst.copy()
    new_lst.append("apple")
    print(new_lst)

def add_one(num: int):
    '''adds one to a number, returns None'''
    num += 1
    print(num)

def main():
    mylist = ["kiwi", "mango"]
    print(f"My list before: {mylist}")
    add_apple_to_list(mylist)
    print(f"My list after: {mylist}")

    number = 1
    print(f"My number before: {number}")
    add_one(number)
    print(f"My number after: {number}")









    # age = int(input("What is your age? "))
    # verdict = can_vote(age)
    # print(verdict)
    # print(get_rps())

    # add_student("Jonathan", age=16, computer="Mac", gender="M")
    # add_student("Liam", gpa=2.0)


main()