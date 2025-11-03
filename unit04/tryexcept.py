'''
try:
    code that might have an error
except [error type]:
    code to run if the try block failed

Put as little code as possible in the try block 
'''

def main():
    # Get int input safely from the user 
    while True:
        try:
            num = int(input("Enter a number: "))
            # if we get here, the user entered an int
            break
            
        except ValueError:
            print("That wasn't an integer. But the program didn't crash")

main()