'''
Split phrase
'''

def main():
    phrase = input("Enter a string: ")

    mid = len(phrase) // 2

    # print the first half 
    print(phrase[:mid])

    # print the second half, one letter on each line 
    for letter in phrase[mid:]:
        print(" "*mid + letter)

main()