'''
9/29/25 
Notes on for loops
'''

def main():
    # Write a program that asks for a string and 
    # prints out anything that isn't a vowel
    text = input("Enter a string: ")
    # loop over each character in the string
    for letter in text:
        # only print the non-vowels
        if letter.lower() not in ["a","e","i","o","u"]:
            print(letter)

    # ask user for a word & give them 10 points for each letter in it
    text = input("Enter a word: ")
    points = 0
    # add 10 for every letter
    for letter in text:
        # make q worth 20
        if letter.lower() == "q":
            points += 20
        else:
            points += 10
    print(points)



main()