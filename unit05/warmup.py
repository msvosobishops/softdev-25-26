def is_palindrome(word: str) -> bool:
    '''returns True if a word is a palindrome, False otherwise'''
    # get rid of spaces
    word = word.replace(" ", "")
    backward_str = word[::-1]
    if word == backward_str:
        return True
    else:
        return False

def range_list(stop:int, start=0, step=1) -> list:
    '''returns a list of range numbers with given start/stop/step'''
    my_list = []
    for i in range(start, stop, step):
        my_list.append(i)
    return my_list

def main():
    print(is_palindrome("nurses ran"))
    print(range_list(start=3, stop=10))

main()