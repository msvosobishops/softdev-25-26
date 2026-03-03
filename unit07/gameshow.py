'''
Game show program 
'''

def get_headers(filename: str) -> list:
    '''Takes in the filename. Opens the file and reads the first line
    to create a list of headers. Returns the list of headers'''
    with open(filename, "r") as file:
        headers = file.readline().strip().split(",")

    return headers

def read_data(filename: str, headers: list) -> list:
    '''Takes in filename and the list of headers.
    Will read all data in the file after the first line and use the headers as keys
    for dictionaries. We will return a list of dictionaries.
    '''
    data = []
    with open(filename, "r") as file:
        # skip the first line
        file.readline()
        # read data in subsequent lines 
        for line in file:
            info = line.strip().split(",")

            # make a dictionary for this line
            person_dict = {}
            for i in range(len(headers)):
                # convert numerical data to int
                if info[i].isnumeric():
                    info[i] = int(info[i])
                person_dict[headers[i]] = info[i]
            
            # add dict to data list 
            data.append(person_dict)
    
    return data


def main():
    headers = get_headers("gameshow.txt")
    data = read_data("gameshow.txt", headers)
    print(data)

    # ask user for name and if it's a contestant, print their age and points 
    name = input("What is your name? ")

    # boolean to keep track of if we found the name 
    name_found = False

    for person in data:
        # person will be a dictionary 
        if name == person['Contestant']:
            print(f"Age: {person['Age']} Points: {person['Points']}")
            name_found = True
        
    if not name_found:
        print("That person isn't a contestant")

main()
