'''
Draw a square
'''

def draw_square(side: int):
    '''prints a square, takes in side length, no returns'''
    for i in range(side):
        print("# " * side)

def main():
    draw_square(6)

main()