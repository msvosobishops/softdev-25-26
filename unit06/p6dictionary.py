'''
Dictionary notes
1/7/26
'''

def shopping_list() -> dict:
    '''asks the user for items/costs, returns a dictionary shopping list'''
    shopping = {}
    while True:
        item = input("What do you want to buy? ")
        if item == "quit":
            break
        cost = float(input("How much does it cost? "))
        # add to dict
        shopping[item] = cost

    return shopping
    


def main():
    # Write a dictionary for your schedule where the keys are your
    # classes and the values are the amount of time spent on 
    # homework for that class 
    schedule = {"Math": 30, 
                "Science": 10, 
                "History": 20,
                "English": 60, 
                "Bib Lit": 10, 
                "Optimal Performance": 0,
                "Software Development": 2,
                "Spanish": 5,
                "Art": 10
                }

    # modify an item
    schedule["English"] = 2
    print(schedule["English"])

    # add an item
    schedule["Dance"] = 0
    print(schedule)

    # remove an item 
    schedule.pop("Bib Lit")
    print(schedule)

    # get method - doesn't cause a KeyError if the key doesn't exist 
    print(schedule.get("calculus"))

    # for loop - when you loop over a dict, you loop over the keys
    for course in schedule:
        print(course)

    # for loop - accessing the values 
    for course in schedule:
        print(schedule[course])

    # for loop - accessing BOTH keys and values
    for key, val in schedule.items():
        print(f"{key} {val} minutes")

    # to access just keys or just values, use the .keys() or .values() methods
    print(list(schedule.values()))

    # shopping list 
    # my_list = shopping_list()
    # print(my_list)




main()