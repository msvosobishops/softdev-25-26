'''
Function for getting a line's x-intercept
'''

def get_line_xint(m: float, b: float):
    '''get the xint of a line, takes in slope and y-int, no returns'''

    # y=0 case
    if m == 0 and b == 0:
        print("There are infinitely many x-intercepts")
    # other horizontal lines 
    elif m == 0:
        print("There is no x-intercept")
    # all other lines
    else:
        x = -b / m 
        print(f"The x-int of y={m}x+{b} is ({x}, 0)")

def main():
    get_line_xint(6, 0)

main()