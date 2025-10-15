'''
Countdown from 10, then blastoff!
'''
import time

def main():
    # countdown from 10
    for i in range(10,0,-1):
        print(f"{i}...")
        # pause for 1 second 
        time.sleep(1)

    # then blastoff! 
    print("BLASTOFF!!!")


main()