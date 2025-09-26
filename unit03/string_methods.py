'''
Ms. Voso 9/25/25
String methods practice
'''

def main():
    # 1 title
    sentence = "coding is fun"
    print(sentence.title())

    # 2 swapcase 
    word = "Coding"
    print(word.swapcase())

    # 3 count
    word = "Beekeeper"
    print(word.count("e"))

    # 4 a couple different options
    sentence = "what does the fox say?"
    print(sentence.count("fox") > 0)
    print(sentence.find("fox") != -1)
    print("fox" in sentence)

    # 5 isupper
    word = "kiran"
    print(word.isupper())

    # 6 replace
    sentence = "henry is in this class"
    print(sentence.replace("henry", "caden"))

    # 7 strip
    sentence = "  Hello, world  "
    print(sentence.strip())

    # 8 find
    sentence = "I ate ten tacos"
    print(sentence.find("taco"))

main()