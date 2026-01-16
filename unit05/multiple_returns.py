'''
Functions that return multiple things
'''

def midpoint(x1:float, y1:float, x2:float, y2:float) -> tuple[float]:
    '''takes in coordinates for 2 points and returns x,y coordinates of midpoint'''
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return mid_x, mid_y 

def main():
    xAB, yAB = midpoint(2, 4, 6, 10)
    xBC, yBC = midpoint(6, 10, 7, -3)
    x, y = midpoint(xAB, yAB, xBC, yBC)
    print(f"Midpoint: ({x}, {y})")

main()