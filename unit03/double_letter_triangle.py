'''
Double letter triangle
'''

def main():
    my_string = input("Enter a string: ")
    double = ""

    for letter in my_string:
        double += letter * 2
        print(double)


main()