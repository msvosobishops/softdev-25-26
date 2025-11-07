def main():
    string = input("Enter a string: ")
    unique_letters = []
    letter_counts = []

    for char in string.lower():
        # add a unique letter to the list 
        if char not in unique_letters:
            unique_letters.append(char)
            letter_counts.append(1)
        # add to the letter counts if the letter is not unique 
        else:
            # get the position the char appears in the list 
            i = unique_letters.index(char)
            # add to corresponding position in letter counts 
            letter_counts[i] += 1
    
    # display nicely
    print(f"{'Letter':<20} Count")
    for i in range(len(unique_letters)):
        print(f"{unique_letters[i]:<20} {letter_counts[i]}")
        


main()