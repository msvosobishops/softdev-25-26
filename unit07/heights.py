'''
A program that asks the user for the height of people in the class 
and writes the information to a text file
'''

def main():
    with open("heights.txt", "w") as file:
        # any code relating to the file goes here, indented 
        # the file will close after this indented block
        file.write("Hello\n")
        file.write("It's me\n")
        file.write("Hello from the other side\n")

main()