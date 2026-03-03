'''
Write a program to read in the data from sleep.txt and save it in a
list. 
Then, calculate the average, min, and max amounts of sleep 
Extension: calculate the mode, median, IQR
'''

def main():
    with open("sleep.txt","r") as file:
        line = file.readline()
        data = line.split(",")

        # convert data to floats, not str 
        for i in range(len(data)):
            data[i] = float(data[i])

        print(data)

    # analytics go here
    

main()