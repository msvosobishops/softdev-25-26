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

    # Get a word from the user and give them 10 points for every 
    # letter in the word
    word = input("Enter a word: ")
    points = 0
    for letter in word:
        # make q worth 20 points 
        if letter == "q":
            points += 20
        else:
            points += 10
    print(f"Points: {points}")



main()