def main():
    string = input("Enter a string: ")

    # first, middle, last letter 
    mid = len(string) // 2
    print(string[0] + string[mid] + string[-1])

    # middle three letters 
    print(string[mid-1 : mid+2])

    # insert BAM into the middle 
    bam = string[0:mid] + "BAM" + string[mid:]
    print(bam)


main()