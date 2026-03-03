'''
Program to get peoples heights and save them
in a text file
'''

def main():
    # w means write mode 
    # will completely overwrite any existing file with this name
    with open("heights.txt", "w") as file:
        while True:
            h = input("What is your height? ")
            if h == "" or h == "quit":
                break
            file.write(h + "\n")

        file.write("The End")

    print("Now we are done with the file")
            

main()