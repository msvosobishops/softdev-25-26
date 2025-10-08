'''
Count how many times 67 appears in a string
'''

def main():
    my_string = input("Enter a string: ")
    
    counter = 0
    # this will store the previous letter as we go through the string
    og = ""

    for letter in my_string:
        if og == "6" and letter == "7":
            counter += 1
        
        # at the end of the loop, set og to = letter 
        # so we'll have the previous letter stored for the next loop
        og = letter

    print(f"no cap 67 appeared {counter} times")

main()