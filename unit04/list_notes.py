'''
List notes
'''

def main():
    # Make a list of at least 5 favorite foods 
    fav_foods = ["pizza", "ice cream", "burritos", "ramen", "french fries"]

    # Accessing
    print(fav_foods[1])

    # Changing 
    fav_foods[4] = "pad thai"
    print(fav_foods)

    # Appending 
    fav_foods.append("soup dumplings")
    print(fav_foods)

    # Negative Indexing - use to count from the end of the list backwards
    print(fav_foods[-1])

main()