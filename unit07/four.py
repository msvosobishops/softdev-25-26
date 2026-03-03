'''
A program to read in the four words from four.txt
'''

def main():

    with open("four.txt", "r") as file:
        # read one line 
        first_line = file.readline().strip()

        # read the rest of the lines 
        other_lines = []
        for line in file:
            other_lines.append(line.strip())

        print(first_line)
        print(other_lines)

main()