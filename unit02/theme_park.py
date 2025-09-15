'''
Ms. Voso 9/11/25
Program to check if a user can ride on a roller coaster
'''

def main():
    # get input from user 
    age = int(input("What is your age? "))
    height = int(input("What is your height in inches? "))
    adult_with = input("Do you have an adult with you? ").lower()
    heart_condition = input("Do you have a heart condition? ").lower()

    # determine whether they can ride on the roller coaster 
    # under 42in or under 12 yrs old cannot ride
    if height < 42 or age < 12:
        print("Sorry, you cannot ride the roller coaster.")
    # over 65 and heart condition cannot ride
    elif age > 65 and heart_condition == "yes":
        print("Sorry, you cannot ride the roller coaster.")
    # between 42-47 inches tall need an adult to ride
    elif 42 <= height <= 47 and adult_with == "yes":
        print("You may ride the roller coaster with an adult.")
    # over 48in tall can ride
    elif height >= 48:
        print("You may ride the roller coaster.")
    # anyone else cannot ride
    else:
        print("Sorry, you cannot ride the roller coaster.")
    
    

main()