'''
Number guessing game!
'''
import random

def main():
    # counter for number of wins
    wins = 0

    # money for wagering
    wallet = 100

    while wins < 3:
        # get user and comp guesses 
        # ensure the input is valid 
        while True:
            user = int(input("guess (1-5): "))
            # only break when the user enters something valid, otherwise they retry
            if 1 <= user <= 5:
                break

        wager = int(input("wager amount: "))

        comp = random.randrange(1,6)

        # check if user was correct, add to the wins counter
        if user == comp:
            wins += 1
            wallet += 3 * wager
            print(f"You and the computer both guessed {user}")
            print(f"Good job! That is {wins} won so far")

        # if user was incorrect
        else:
            wallet -= wager
            print(f"User guesses {user} and computer guessed {comp}")
            print("Let's try again")

        print(f"You have ${wallet} left")

    # If we're outside the while loop, the user must've won 3 times
    print("YOU WIN!")

main()