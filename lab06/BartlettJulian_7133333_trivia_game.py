'''
Julian, Noah, 1/30/26
'''

import time
import random
import requests
import html

def intro():
    '''introduces program and its rules'''
    print("Welcome to Money Mayhem!")
    time.sleep(1)
    print("You will pick your difficulty, and have three lives to answer questions.")
    time.sleep(1)
    print("You can quit whenever you have one life remaining, and if you lose your money gets divided by 10.")
    time.sleep(1)
    print("You start with $100 and will have your money double if you get a question correct, and half if wrong you get a question wrong.")
    time.sleep(1)
    print("Good luck!")
    print("-"*30)

def get_difficulty() -> int:
    '''Gets difficulty of each question, returns number of lives'''
    while True:
        question_difficulty = input("Easy, medium, or hard? ").lower()
    
        if question_difficulty == "easy":
            lives = 3
            break
        elif question_difficulty == "medium":
            lives = 3
            break
        elif question_difficulty == "hard":
            lives = 3
            break
        else:
            print("That is not a possible difficulty. Please enter one of the 3 options.")

    return question_difficulty, lives

def get_questions(question_difficulty: str):
    '''Takes in difficulty and returns a set of 
    20 questions based on the difficulty'''

    while True:
        time.sleep(2)
        if question_difficulty == "easy":
            response = requests.get("https://opentdb.com/api.php?amount=20&difficulty=easy&type=multiple").json()
        elif question_difficulty == "medium":
            response = requests.get("https://opentdb.com/api.php?amount=20&difficulty=medium&type=multiple").json()
        else:
            response = requests.get("https://opentdb.com/api.php?amount=20&difficulty=hard&type=multiple").json()
        response_code = response.get("response_code")
        if response_code == 0:
            break
    return response

def ask_question(response: list, lives: int, i: int):
    '''Takes in the response code, the current amount of lives, 
    and the question number, and asks a question'''
    answers = []
    print(30*"-")
    results = response.get("results")
    print(html.unescape(results[i]['question']))
    answer = html.unescape(results[i]['correct_answer'])
    for k in range(3):
        answers.append(html.unescape(results[i]['incorrect_answers'][k]))
    
    # shuffles answers
    answers.append(answer)
    random.shuffle(answers)
 
    # converts answers to letters
    a = answers[0]
    b = answers[1]
    c = answers[2]
    d = answers[3] 
    if a == answer:
        answer_letter = "A"
    elif b == answer:
        answer_letter = "B"
    elif c == answer:
        answer_letter = "C"
    else:
        answer_letter = "D"
    
    print(f"A: {a}, B: {b}, C: {c}, D: {d}")
    user_answer = input("A, B, C, or D? ").capitalize()
    print(30*"-")
    if user_answer == answer_letter or user_answer == answer:
        print("Correct!")
        return "correct", lives
    else:
        print(f"Incorrect. The correct answer was {answer_letter}: {answer}.")
        lives -= 1
        return "wrong", lives
        
def main():
    intro()
    #question number
    i = 0
    money = 100
    question_difficulty, lives = get_difficulty()
    response = get_questions(question_difficulty)
    while True:
        success, lives = ask_question(response, lives, i)
        #if you have no lives you get a tenth of your money
        if lives == 0:
            money = money * 0.1
            print(30*"-")
            print(f"You lost your money, looks like someone got greedy! You get ${money}.")
            break
        if success == "correct":
            i += 1
            print(30*"-")
            money = money * 2
            print(f"You won ${money/2}. Your new total is ${money}")
            print(f"You have {lives} lives left.")
        elif success == "wrong":
            #halve money if wrong
            i += 1
            print(30*"-")
            money = money/2
            print(f"Your money had been halved. Your new total is ${money}")
            print(f"You have {lives} lives left.")
        if lives == 1:
            #can quit if one life left
            quit_game = input("You have one life left. Would you like to quit? "
                            "Enter y to quit, and n if you wish to continue: ")
            if "y" in quit_game:
                print(f"Congratulations. You won ${money}!")
                break
main()