'''
Get a letter from the user and print whether it is a vowel
'''

def main():
    # get the letter from the user
    letter = input("Give me a letter: ")

    # list of vowels
    vowels = ["a", "e", "i", "o", "u"]

    # check if letter (as lowercase) is in the vowels list
    if letter.lower() in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is NOT a vowel")



main()