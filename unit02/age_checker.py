'''
Ms. Voso 9/8
Program to check user's age and tell them if they can vote
'''

def main():
    # get age as an int
    age = int(input("What is your age? "))

    # check if they are over 18
    if age >= 18:
        print("You can vote!")
    # check if they are over 16 (but under 18)
    elif age >= 16:
        print("You can almost vote!!!")
    # check if they are under 2
    elif age <= 2:
        print("You're a baby. You can't vote.")
    # anyone else is between 2 to 16
    else:
        years_until_voting_age = 18 - age
        print(f"You are not old enough to vote. You can vote in {years_until_voting_age} years.")
    

main()