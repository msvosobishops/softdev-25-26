def main():
    word = input("enter a phrase: ")

    # index of the middle 
    middle = len(word) // 2

    # print first half 
    print(word[:middle])

    # loop to print second half
    for letter in word[middle:]:
        print(" "*middle + letter)

main()