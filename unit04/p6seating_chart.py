'''
Random Seating Chart Program
'''

import random 

def main():
    students = ['Ari', 'Minh', 'Anya', 'Charlotte', 'Laura', 'Cady', 
                'Isabelle', 'Katelyn', 'Yuna', 'Julian', 'Ian', 'Noah',
                'David', 'Jonah', 'Brooke']

    # remove absent students 
    remove_absent = input("Is anyone absent? (y or n) ")
    if remove_absent.lower() == 'y':
        # loop to remove absent students
        while True:
            person = input("Enter absent student. (q to quit) ")
            # only remove students in the list (to avoid error)
            if person.capitalize() in students:
                students.remove(person.capitalize())
            # q to quit
            if person == "q":
                break

    # randomize the students in the list 
    random.shuffle(students)

    # Ask the user how many groups they want 
    # Split the class into that many groups (approx the same size)
    n = int(input("How many groups? "))
    group_size = len(students) // n 
    remainder = len(students) % n 

    # initial start and stop value
    start = 0
    stop = 0
    for i in range(n):
        stop += group_size
        # add an extra person to some groups 
        if i < remainder:
            stop = stop + 1
        # print the groups 
        print(f"Table {i+1}: {students[start:stop]}")

        # set start value for next loop 
        start = stop
    


main()