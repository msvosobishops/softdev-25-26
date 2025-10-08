'''
Triangle using range loop
'''

def main():
    char = input("Give me a character: ")
    n_rows = int(input("Give me a number of rows: "))

    # Different ways this could be implemented
    # option 1
    for i in range(n_rows):
        print(char * (i+1))

    # option 2
    for i in range(1, n_rows+1):
        print(char * i)

    # option 3 - string accumulator
    new_string = ""
    for i in range(1, n_rows+1):
        new_string += char
        print(new_string)


main()