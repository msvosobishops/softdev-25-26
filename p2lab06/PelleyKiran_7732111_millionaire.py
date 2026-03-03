'''
kiran and caden
27 january 2026
who wants to be a millionaire game

sources used:
https://marketplace.visualstudio.com/items?itemName=iliazeus.vscode-ansi
    ansi color database for color text formatting
'''

import requests 
import html 
import random
import time

def prize_money(question_number: int)-> int:
    '''returns the prize money list and is accessed by parameter for question number'''
    money = [500,1000,2000,3000, 5000, 7500, 10000,15000, 25000, 50000, 75000, 
            150000, 250000, 500000, 1000000]
    return money[question_number]

def checkpoints(question_number: int) -> int:
    '''returns the users final $$ if they lose and once they reach a certain question'''
    if question_number < 5: 
        return 0
    elif question_number < 10:
        return 5000
    elif question_number < 15: 
        return 50000

def ask_question(results: dict, question_number: int):
    '''asks the question given the contents and question number'''
    # make list with all the possible answers, from the results dictonary
    choices = results[question_number]['incorrect_answers']
    # append list wiht the correct answer and make sure it is html.unescape
    choices.append(results[question_number]['correct_answer'])
    # print the question
    print(f"\n{html.unescape(results[question_number]['question'])}")
    print()

    # print("\x1b[32m" + html.unescape(results[question_number]['correct_answer']) + "\x1b[0m")
    # print()

    

    choices.sort()
    # print each option without list formatting
    for option in choices:
        print(html.unescape(option))

    print()

def check_ans(results: dict, question_number: int) -> bool:
    '''
    purpose: checks if the question is correct  
    parameters: question number and content of the questions (from api)
    returns: true if correct or false if incorrect or done playing
    '''

    # call function to display question and answers
    ask_question(results, question_number)

    # get user input
    answer = input("Your answer: ")
    # check if correct
    if answer.lower() == results[question_number]['correct_answer'].lower():
        
        # set variable for money earned
        won = prize_money(question_number)

        print(f"Correct! You've won \x1b[33m${prize_money(question_number)}\x1b[0m")
        question_number += 1

        print()
        
        # check if user wants to continue playing
        if question_number != 15:
            continue_playing = input(f"Press ENTER to continue or 'quit' to walk away with \x1b[33m${won}\x1b[0m ")
            if continue_playing.lower() == 'quit':
                print(f"Okay, you get to walk away with \x1b[33m${won}\x1b[0m")
                return False
            else:
                return True
        else:
            return True
    else:
        # ensure they go home with some money if they have reached a checkpoint
        cor_ans = html.unescape(results[question_number]['correct_answer'])
        money = checkpoints(question_number)
        print(f"\x1b[91mYou lost\x1b[0m, the correct answer is \x1b[32m{cor_ans}\x1b[0m. You walk away with \x1b[33m${money}\x1b[0m")
        return False


def main():
    # store question values from open database
    # alternate link: "https://opentdb.com/api.php?amount=15&difficulty=easy&type=multiple"
    response = requests.get("https://opentdb.com/api.php?amount=15&category=22&type=multiple").json()

    # ensure API will output the questions
    response_code =  response.get("response_code")
    results = response.get("results")

    if response_code == 0:
        # Introduce the user to the experience
        print("\nWelcome to \x1b[3m\x1b[1mWho Wants to be a Millionaire!\x1b[0m")
        print("-" * 50)
        time.sleep(1)
        print("Answer the question given to you among the four answers.")
        time.sleep(.5)
        print("There are 15 questions in total, and you must get them right to continue")
        time.sleep(.5)
        print("You get checkpoints after winning $5000 and $50000.")
        time.sleep(.5)
        print("Make sure your answer is spelled correctly(punctuation matters)")
        time.sleep(.5)
        print()
        # print all info for the first question
        
        # counter for question number (tells program when to stop)
        counter = 0
        # ask user if they are ready to start
        input("press ENTER to continue")
        still_playing = True
        # repeatedly ask questions
        while still_playing == True:
            # call question
            still_playing = check_ans(results, counter)
            counter += 1
            # finish if they win
            if counter == 15 and still_playing == True:
                print("You won the Grand Prize!")
                break

    else:
        print("Oops try again")
main()