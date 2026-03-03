'''
Read in quiz-grades.txt
Create a dictionary where the key is the name and the value is a list of grades 
'''

def main():
    grades_dict = {}
    with open("quiz-grades.txt", "r") as file:
        # loop over lines in the file 
        for line in file:
            # info will be a list of strings 
            info = line.strip().split(",")
            name = info[0]
            grades = info[1:]

            # convert the grades to ints 
            for i in range(len(grades)):
                grades[i] = int(grades[i])

            # add to the dict
            grades_dict[name] = grades

    print(grades_dict)

    # average the grade 
    for name, grades in grades_dict.items():
        avg = sum(grades) / len(grades)
        print(f"{name}: {avg}")

main()