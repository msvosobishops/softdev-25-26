'''
A program to create a seating chart for class
'''
import random

def main():
    students = ['Kiran', 'Fei-Lian', 'Ashali', 'Caden',
                'Henry', 'Jaden', 'Connor', 'Theo', 
                'Michael', 'Benny', 'Daniel', 'Alice',
                'Emma']

    # randomly mix up the list 
    random.shuffle(students)

    # Ask the user how many tables 
    # Divvy up the students amongst those 
    n = int(input("How many tables? "))
    group_size = len(students) // n 
    remainder = len(students) % n 

    start = 0
    stop = group_size
    for i in range(n):
        # add the extra students to the first few groups 
        if i < remainder:
            stop += 1

        print(f"Table {i+5}: {students[start : stop]}")
        # change start and stop for next loop
        start = stop
        stop += group_size

main()