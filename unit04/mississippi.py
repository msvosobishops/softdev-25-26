'''
Program that uses parallel lists to count how many times each character appears in a string
'''


def main():
    string = input("Enter a string: ")
    letters = []
    counts = []

    for char in string.lower():
        # add a unique letter to the list 
        if char not in letters:
            letters.append(char)
            counts.append(1)
        # add to the letter counts if the letter is not unique 
        else:
            # find the position where the char occurs 
            position = letters.index(char)
            # modify the count for that letter 
            counts[position] += 1

    # print everything nicely 
    # headers 
    print(f"{'Letters':<10} Counts")
    # letters and counts
    for i in range(len(letters)):
        print(f"{letters[i]:<10} {counts[i]}")
            
    
        


main()