'''
Number guessing game!
'''
import random

def main():
    while True:
        # make sure input is valid. Try again if not.
        while True:
            user = int(input("guess (1-5): "))
            # if guess is valid, break. Otherwise, ask for input again
            if 1 <= user <= 5:
                break

        comp = random.randrange(1, 6)

        if user == comp:
            print("You win!")
            break
        
        else:
            print(f"You guessed {user} and the computer guessed {comp}")
            print("Let's try again")

main()