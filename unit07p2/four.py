'''
Program to read the file four.txt
'''

def main():
    # r means read mode 
    with open("four.txt", "r") as file:
        first_word = file.readline().strip()
        print(first_word)

        rest_of_the_words = []
        for line in file:
            rest_of_the_words.append(line.strip())
        print(rest_of_the_words)


main()