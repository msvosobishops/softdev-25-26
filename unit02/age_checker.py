'''
Ms. Voso 9/8
Program to check user's age and tell them if they can vote
'''

def main():
    # get the user's age as an int
    age = int(input("What is your age? "))

    # check if they are 18+
    if age >= 18:
        print("You can vote!")
    # if they're 16 or 17
    elif 16 <= age <= 17:
        print("You can almost vote! But you can already drive.")
    # if they're a small child 
    elif age <= 2:
        print("You're a baby.")
    # else they are between 3 to 15
    else:
        years_until_vote = 18 - age
        print(f"Unfortunately you can't vote. You have to wait {years_until_vote} years")

    

main()