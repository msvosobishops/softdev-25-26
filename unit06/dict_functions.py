def unique_values(dictionary: dict) -> list:
    '''takes in a dict and returns a list of the unique values in that dict'''
    
    uniques = []

    # loop over values only
    for value in dictionary.values():
        # only add a unique value to the list 
        if value not in uniques:
            uniques.append(value)

    return uniques

def key_exists(dictionary: dict, key: str) -> bool:
    '''takes in a dict and a key, return True if the key is in the dict, False otherwise'''
    # Note: in keyword will only check the keys, not the values
    if key in dictionary:
        return True
    else:
        return False

def get_keys(dictionary: dict, value) -> list:
    '''takes in a dictionary and a value and returns a list of keys with that value'''
    keys = []

    for key, val in dictionary.items():
        # check if the val is the target value 
        if val == value:
            keys.append(key)

    return keys

def lists_to_dict(list1: list, list2: list) -> dict:
    '''takes in two lists of the same size and returns a dictionary
    list1 becomes the keys, list2 becomes the values'''

    # return None if the lists are not the same length
    if len(list1) != len(list2):
        return

    d = {}
    for i in range(len(list1)):
        key = list1[i]
        value = list2[i]
        # add new key value pair to dictionary
        d[key] = value

    return d

def main():
    dictionary = {"a": 1, "b": 2, "c": 1, "d": 3}
    print(unique_values(dictionary))
    print(key_exists(dictionary,"a"))
    print(key_exists(dictionary,"z"))
    print(get_keys(dictionary, 5))
    print(lists_to_dict([1,2,3], [4,5,6]))

main()