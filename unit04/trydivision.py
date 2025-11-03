'''
A very safe program that gets two numbers from the user and divides them
'''

def main():
    # Get the first number 
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Whoops that wasn't a number! Try again.\n")

    # Get the second number 
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Whoops that wasn't a number! Try again.\n")

    try:
        print(f"{num1} / {num2} = {num1/num2}")
    except ZeroDivisionError:
        print(f"{num1} / {num2} is undefined")
        


main()