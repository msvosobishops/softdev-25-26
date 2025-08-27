'''
Ms. Voso 8/27/25
A program that calculates the cost of school
'''

def main():
    # get input from the user 
    name = input("Name: ")
    # convert tuition and fin aid to int
    tuition = int(input("Tuition: "))
    financial_aid = int(input("Financial Aid: "))

    # calculate amount owed 
    bill = tuition - financial_aid

    # print message 
    print(f"Hi, {name}! Your bill is ${bill}")


main()