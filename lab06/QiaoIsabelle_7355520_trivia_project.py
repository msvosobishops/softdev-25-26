'''
Yuna Shi, Isabelle Qiao, Brooke Gibbons, 26/01/2026, trivia project
'''
import requests
import html
import time

# used google search to learn how to use colorama to change font colours
# link: https://www.geeksforgeeks.org/python/introduction-to-python-colorama/
from colorama import Fore, Style


def give_instructions():
    '''gives the user personalised instructions for the game if they need them'''
    name = input("\nHi! Welcome to Jeopardy! What's your name? ")

    while True:
        rules = input(Fore.BLACK + f"Welcome, {name}! Have you played Jeopardy before? (Y/N): ").upper()
        if rules == "Y" or rules == "N":
            break
        else:
            print(Fore.RED + "Please enter either 'Y' or 'N'.")
    
    if rules == "Y":
        print("\nAlright then, let's get started!")
    elif rules == "N":
        print(f"\nOkay, {name}, here's a quick runthrough:\n")
        print("You will pick a category and difficulty level based on the " \
        "questions left on the board, $100 being the easiest and $300 " \
        "being the hardest.")
        print("If you get the question correct, you win the amount of money that your " \
        "question is worth. Or else, you win nothing.")
        print("After each round, you will have a choice to end the game. The game " \
        "will automatically end after 15 rounds.")
        print("Your final prize money will be displayed at the end of the game.\n")
        play = input("Press ENTER to start playing. ")
        print(Fore.MAGENTA + f"\n\nHave fun, {name}!")
        print(Style.RESET_ALL)
        

def get_pos_and_question_dict() -> list:
    '''returns the grid positions (list) and question dictionary (dict); acts as storage'''

    # display of positions on grid (also shows which questions remain to be answered)
    pos = ["100", "100", "100", "100", "100",
        "200", "200", "200", "200", "200", 
        "300", "300", "300", "300", "300",]

    # dictionary to find the properties of the question user wants to answer:
    # category, level, and position on grid
    questions_dict = {
        "math100": ["math", "easy", 0],
        "math200": ["math", "medium", 5],
        "math300": ["math", "hard", 10],
        "history100": ["history", "easy", 1],
        "history200": ["history", "medium", 6],
        "history300": ["history", "hard", 11],
        "art100": ["art", "easy", 2],
        "art200": ["art", "medium", 7],
        "art300": ["art", "hard", 12],
        "geography100": ["geography", "easy", 3],
        "geography200": ["geography", "medium", 8],
        "geography300": ["geography", "hard", 13],
        "sports100": ["sports", "easy", 4],
        "sports200": ["sports", "medium", 9],
        "sports300": ["sports", "hard", 14],        
        }
    
    return pos, questions_dict


def retrieve_api_question(category_name: str, difficulty: str) -> str:
    '''takes in a category and difficulty, returns a question from open.api'''

    # maps each cater=gory name to its assigned number in open-api
    catagorical_defs = {
        "sports": 21,
        "geography": 22,
        "art": 25,
        "history": 23,
        "math": 19,
    }

    # finds the open-api assigned number of the category and stores it as a variable
    category = ""
    for key, value in catagorical_defs.items():
        if key == category_name:
            category = value

    # get and return a multiple-choice question with specified category and difficulty
    question = requests.get(f"https://opentdb.com/api.php?amount=1&category={category}&difficulty={difficulty}&type=multiple").json()
    return question


def print_board(pos: list):
    '''takes in the current board positions and prints the current board'''

    print(Fore.BLUE)
    print(" math" + "  |  " + "history" + "  |  " + "art" + "  |  " + "geography"
             + "  |  " + "sports")
    print("-" * 50)
    print("  " + pos[0] + "  |    " + pos[1] + "    |  " + pos[2] + "  |     " + pos[3]
             + "     |  " + pos[4])
    print("-" * 50)
    print("  " + pos[5] + "  |    " + pos[6] + "    |  " + pos[7] + "  |     " + pos[8]
             + "     |  " + pos[9])
    print("-" * 50)
    print("  " + pos[10] + "  |    " + pos[11] + "    |  " + pos[12] + "  |     " + pos[13]
             + "     |  " + pos[14])
    print(Style.RESET_ALL)


def get_user_question_choice() -> str:
    '''asks and gets user's category and level choice for the question'''

    # loop to ensure a valid input from user
    while True:
        category_user = input(Fore.CYAN + "Please enter a category: ")
        if category_user.lower() not in ["math", "history", "art", "geography", "sports"]:
            print(Fore.RED + "Please select a valid category.\n")
        else:
            break

    # loop to ensure a valid input from user
    while True:
        level_user = input(Fore.CYAN + "Please enter the level (100, 200, or 300): ")
        if level_user.lower() not in ["100", "200", "300"]:
            print(Fore.RED + "Please select a valid level.\n")
        else:
            break
    
    # change text colour back to normal
    print(Style.RESET_ALL)
    
    return category_user, level_user


def get_a_question(question_details: list) -> list:
    '''gets a question from the api database. if a server overload error occurs, 
    continues trying again every five seconds until question is obtained.'''
    while True:
        # get a question from the api & store 'response code' and 'question lists'
        api = retrieve_api_question(question_details[0], question_details[1])
        response_code = api.get("response_code")
        question = api.get("results")

        # check if question retrieval was successful (response code = 0), and if 
        # question is valid for the game (no "which"). if not successful, try again after 5 secs
        if response_code == 0 and "which" not in str(question[0]["question"]).lower():
            break
        else:
            print("Loading...")
            time.sleep(5)
        
    # return the question
    return question


def end_sequence(prize_money: int):
    '''prints the end sequence after the user has finished the game, and tells
    user how much prize money they won'''

    # gives different end text if user didn't answer anything correct
    if prize_money == 0:
        print(Fore.LIGHTRED_EX + "\n\nYou won $0... maybe polish up on your trivia "
              "a bit. Thanks for playing!\n")
    else:
        print(Fore.GREEN + f"\n\nCongratulations! You won ${prize_money}. "
              "Thanks for playing!\n")


def main():
    # greets and gives the user instructions if they need
    give_instructions()

    # count how many rounds have passed
    rounds = 0
    # variable for cumulative prize money won
    prize_money = 0
    # retrieves the stored grid position list and question type dictionary
    pos, questions_dict = get_pos_and_question_dict()

    # repeats the game until all 15 questions are done or until player breaks
    while rounds != 15:
        # displays round number and current prize money
        print(Fore.CYAN + f"\n\nRound {rounds + 1}:")
        print(Fore.BLACK + f"Current Prize Money: ${prize_money}")

        # print the board
        print_board(pos)

        # user selects a category and level of question. checks to see if question
        # is available to answer
        while True:
            category_user, level_user = get_user_question_choice()

            # gets the corresponding question details from the dictionary of 
            # question types (a format that the api url accepts)
            for key, value in questions_dict.items():
                if key == category_user.lower() + (level_user):
                    question_details = value 

            # checks if the question has already been taken. If it has, prompts 
            # user for another question selection
            if pos[question_details[2]] != "   ":
                break
            else:
                print("This question is not available. Please choose another.\n")
        
        # gets a question corresponding to the properties that user wants
        question = get_a_question(question_details)

        # gets user's answer to the question
        print()
        user_answer = input(html.unescape(question[0]["question"]) + " ")
    
        # if the user gets the question correct, give them the prize money of the 
        # question. else, tell them what the correct answer was
        if user_answer.lower() == str(question[0]["correct_answer"]).lower():
            print(Fore.GREEN + f"Correct! +${level_user}")
            prize_money += int(level_user)
        else:
            print(Fore.RED + f"Incorrect! The answer was {html.unescape(question[0]["correct_answer"])}.")
        
        # remove the question from list of available questions
        pos[question_details[2]] = "   "

        # print board after question is asked (delay for aesthetics)
        time.sleep(0.5)
        print_board(pos)

        # one round has passed
        rounds += 1

        # checks if player wants to stop playing (if there's still rounds left in game)
        if rounds != 15:
            stop = input(Fore.MAGENTA + "To quit, press 'q'. Or else, input any value. ")
            if stop.lower() == "q":
                break

    # runs the game end sequence
    end_sequence(prize_money)


main()