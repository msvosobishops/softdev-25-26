'''
A program to get a word from the user and make a new string with
the vowels removed
'''

def main():
    my_string = input("Enter a string: ")
    new_string = ""

    for char in my_string:
        # only add non-vowels 
        if char.lower() not in ["a","e","i","o","u"]:
            new_string += char
    
    print(new_string)

main()