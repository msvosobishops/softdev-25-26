'''
Anya Maru and Katelyn Chan
January 26th, 2026
https://opentdb.com/
'Who Wants to Be Rich? (Trivia Game)'
'''

'''
ideas:
- 4 lifelines: (2)50/50, (2)reveal the answer
- color print
- prices: 100, 200, 300, 500, *1000, 2000, 4000, 8000, 16000, *32000, 64000, 125000, 250000, 500000, *1 mil, 10 mil, 25 mil, *50 mil, 100 mil, wager???
- choose to leave (keep amnt of money)
- difficulty
'''
import requests
import html
import time
# Note to Ms. Voso: install colorama --> https://youtu.be/u51Zjlnui4Y?si=J_P5h-uUtNSZbBK2
from colorama import Fore


def intro():
    '''print out intro statement for game, no parameters or returns'''
    print()
    print("WELCOME TO 'WHO WANTS TO BE RICH?' In this game, YOU will have the opportunity to win $100 million OR MORE! \n" \
    "Rules of the Game: We will ask you a series of questions. The more you answer correctly, the more MONEY you win! \n" \
    "You will have 2 'lifelines': 'reveal the answers', which will serve as a free pass. \n" \
    "When you use these lifelines, you WILL earn the alloted amount for that question.  \n" \
    "You will have the option to walk out with however much you have accumulated, \nHOWEVER if you answer incorrectly, your time with us will have ended. \n" \
    "If you would like to use a lifeline or would like to walk out, please type 'Lifeline' or 'Walk Out' when the question is asked. \n" \
    "You may receive a sum of $1,000, $8,000, $32,000, $250,000, $1 million, or $50 million as checkpoints." \
    "\nGood Luck!")
    print()

def get_data()->dict:
    '''get response code from API, no parameters, returns dictionary of question info'''
    while True:
        response = requests.get("https://opentdb.com/api.php?amount=20&difficulty=easy").json()
        response_code = response.get("response_code")
        # if success
        if response_code == 0:
            med_data = response.get("results")
            intro()
            return med_data
        # repeat if not successful
        time.sleep(1)

def ask_questions(med_data:dict, amount: list, i: int, wager: float)->str:
    '''retrieves questions and answers (from med_data), loop through amount earned, returns the correct answer'''
    question = html.unescape(med_data[i]["question"])
    correct_answer = html.unescape(med_data[i]["correct_answer"])
    if i < 18:
        print(Fore.CYAN, f"For ${str(amount[i])}: {question}")
    else:
        print(Fore.CYAN, f"For ${wager}: {question}")
    return correct_answer
            
def check_answers(i: int, correct_answer: str, amount: list, lifelines: int, earnings: int)->tuple[int,str]:
    '''loops over questions using amount and i, compares user input with correct answer (provides earnings), return lifelines and status'''
    answer = str(input("Enter the answer: ")) 
    print()
    # compare answers
    if answer.upper() == correct_answer.upper():
        earnings = amount[i]
        print(Fore.GREEN, f"That is correct! You're at ${earnings}! Next question :D")
        print()
    # if user wants to use lifelines
    elif answer.upper() == "LIFELINE":
        if lifelines > 0:
            lifelines = using_lifelines(amount, correct_answer, i, lifelines, earnings)
        else:
            earnings = amount[i-1]
            final = get_amount_earned(earnings)
            print(Fore.MAGENTA, f"You're out of lifelines! Be careful next time :( You ended with ${final}!")
            print()
            return lifelines, "Game over!"
    # if user wants to walk out
    elif answer.upper() == "WALK OUT":
        print(Fore.MAGENTA, f"You have walked out with ${amount[i-1]}! Feel free to try again or join us next time :D")
        return lifelines, "walk out"
    # if user incorrectly answered
    else:
        if i == 0:
            earnings = 0
        else:
            earnings = amount[i-1]
        final = get_amount_earned(earnings)
        print(Fore.RED, f"THAT IS INCORRECT! I'm sorry, the answer is {correct_answer}, you have LOST this game." \
                f"You have earned ${final}! Feel free to try again or join us next time :D")
        return lifelines, "Game over!"
        # why we use return: https://mimo.org/glossary/python/return
    return lifelines, "worked"
           
def using_lifelines(amount: list, correct_answer: str, i: int, lifelines: int, earnings: int)->int:
    '''calculate and return # of lifelines'''
    lifelines -= 1
    earnings = amount[i]
    print(Fore.MAGENTA, f"You used a lifeline! You are at {lifelines} lifeline(s). The correct answer was '{correct_answer}'. You are at ${earnings}!")
    print()
    return lifelines

def get_amount_earned(earnings: int)->int:
    '''takes in total earning after game is played, returns amount based on game rules'''
    if earnings < 1000:
        final = 0
    elif earnings < 8000:
        final = 1000
    elif earnings < 32000:
        final = 8000
    elif earnings < 250000:
        final = 32000
    elif earnings < 1000000:
        final = 250000
    elif earnings < 50000000:
        final = 1000000
    return final

def get_wager(med_data: dict, amount: list)->float:
    '''asks user for input and adds/subsracts from earnings depending on wager'''
    earnings = 100000000
    wager = float(input("Place your bets: $"))
    correct_answer = ask_questions(med_data, amount, 18, wager)
    answer = str(input("Enter the answer: "))
    print()
    if answer.upper() == correct_answer.upper():
        earnings += wager
        print(Fore.BLACK, f"WOW! YOU'RE SO SMART! You've ended with a score of ${earnings}. Great Job! Feel free to play again :D")
    else:
        earnings -= wager
        print(Fore.BLACK, f"THAT'S INCORRECT. The answer was {correct_answer} You've ended with a score of ${earnings}. Great Job! Feel free to play again :D")


def main():
    # set variables
    amount = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 10000000, 25000000, 50000000, 100000000]
    med_data = get_data()
    earnings = 0
    lifelines = 2
    wager = 0
    # run through game
    for i in range(len(amount)):
        correct_answer = ask_questions(med_data, amount, i, wager)
        lifelines, status = check_answers(i, correct_answer, amount, lifelines, earnings)
        if status == "Game over!":
            return
        elif status == "walk out":
            return
    # wager if reached the end
    get_wager(med_data, amount)
    

main()
