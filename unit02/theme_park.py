'''
Ms. Voso 9/11/25
Program to check if a user can ride on a roller coaster
'''

def main():
    # get inputs from user 
    age = int(input("What is your age? "))
    height = int(input("What is your height in inches? "))
    adult_present = input("Do you have an adult with you? ")
    heart_condition = input("Do you have a heart condition? ")

    # Under 12 or under 42 in
    if age < 12 or height < 42:
        print("Sorry, you cannot ride the roller coaster")
    # Over 65 and heart condition 
    elif age > 65 and heart_condition == "yes": 
        print("Sorry, you cannot ride the roller coaster")
    # Between 42 to 47 inch needs an adult presence
    elif 42 <= height <= 47 and adult_present == "yes":
        print("You may ride the roller coaster with an adult")
    # Over 48 inches
    elif height >= 48:
        print("You may ride the roller coaster alone!")
    # Anyone else cannot ride 
    else:
        print("Sorry, you cannot ride the roller coaster")

        

main()