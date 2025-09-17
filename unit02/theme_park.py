'''
Dominique Voso
Sept 16, 2025 
Program to determine if someone can ride a roller coaster
'''

def main():
    # get input from user 
    age = int(input("What is your age? "))
    height = int(input("What is your height (inches)? "))
    adult_with = input("Do you have an adult with you? ").lower()
    heart_condition = input("Do you have a heart condition? ").lower()

    # check if they can ride the roller coaster 
    # under 42in or under 12 yrs old cannot ride
    if height < 42 or age < 12:
        print("Sorry you cannot ride the roller coaster.")
    # older than 65 can't ride with heart condition 
    elif age > 65 and heart_condition == "yes":
        print("Sorry, you cannot ride the roller coaster.")
    # between 42-47in can ride with adult 
    elif height <= 47 and adult_with == "yes":
        print("You may ride the roller coaster with an adult.")
    # over 48in can ride alone
    elif height >= 48:
        print("You can ride the roller coaster alone!")
    else:
        print("Sorry you cannot ride the roller coaster.")

main()