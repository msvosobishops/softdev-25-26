'''
Dictionary notes 
1/8/26
'''

def create_shopping_list() -> dict:
    '''returns a shopping list dictionary'''
    shopping_list = {}
    while True:
        item = input("What do you want to buy? (say done if finished) ")
        if item == "done":
            break
        cost = float(input(f"How much does {item} cost? "))
        # add to dict
        shopping_list[item] = cost

    return shopping_list


def lists_to_dict():
    keys = ["Ten", "Twenty", "Thirty"]
    values = [10, 20, 30]

    new_d = {}

    for i in range(len(keys)):
        new_d[keys[i]] = values[i]

    print(new_d)

lists_to_dict()


def main():
    # Write a dictionary with the keys being your classes and the values
    # being how much time you spend on homework 
    schedule = {"Math": 30,
                "English": 60,
                "History": 100,
                "Science": 15,
                "Soft Dev": 1,
                "Language": 15,
                "Art": 0
                }
    
    # Access an item in the dictionary 
    print(schedule["Language"])
    schedule["Language"] = 10

    # Add an item to the dictionary 
    schedule["Bib Lit"] = 30

    # Remove 
    schedule.pop("Bib Lit")
    print(schedule)

    # Looping - by default, you loop over the keys 
    for course in schedule:
        print(f"{course} has {schedule[course]} min of HW")

    # Looping over just the values 
    for minutes in schedule.values():
        print(minutes)

    # Looping over the keys and the values 
    for key, val in schedule.items():
        print(f"{key} has {val} minutes of HW")


    # What if I want to find the max value? 
    print(list(schedule.values()))
    print(max(schedule.values()))

    for key, val in schedule.items():
        if val == max(schedule.values()):
            print(key)

    # Get method - doesn't give a KeyError if the key doesn't exist 
    print(schedule.get("PE"))


    print(create_shopping_list())


# main()

