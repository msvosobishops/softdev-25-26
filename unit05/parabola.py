'''
Program to display table of values for a parabola
'''

def parabola(a: int, b: int, c: int):
    '''prints the values of a parabola, takes in 3 coefficients, no returns'''

    print(f"{'x':>10} {'y':>10}")
    print("=" * 21)

    for x in range(-5, 6):
        y = a * x**2 + b*x + c 
        print(f"{x:>10} {y:>10}")

def main():
    a = int(input("What is the value of a? "))
    b = int(input("What is the value of b? "))
    c = int(input("What is the value of c? "))
    parabola(a, b, c)

main()
