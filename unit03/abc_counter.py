'''
A program to count the alpha characters in a string
'''

def main():
    my_string = input("Enter a string: ")
    counter = 0
    for letter in my_string:
        if letter.isalpha():
            counter += 1

    print(counter)

    


main()