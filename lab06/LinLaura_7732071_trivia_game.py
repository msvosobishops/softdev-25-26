'''
1/26/26 Laura & David
Modified Who Wants to be a Millionare Trivia Game
'''

import requests
import html
import random
import time

def gives_instructions():
    '''prints instructions, no parameters, no returns'''
    # tells user how the game works
    print("Answer 10 questions to go up the money ladder. Each one is worth $100.")
    print("If you answer one wrong, you drop to a certain value. (eg. $0, $200, $400, etc.)")
    print("Try to get to $1,000!")

def get_questions() -> dict:
    '''gets API, no parameters, returns questions'''
    # loops to make sure questions and options are generated
    while True:
        # get the response from the API (questions & options)
        response = requests.get("https://opentdb.com/api.php?amount=11").json()
        response_code = response.get("response_code")
        questions = response.get("results")
        # 0 means success
        if response_code == 0:
            break
        else: 
            # wait 5 sec to make sure code runs
            print("please wait...")
            time.sleep(5)
    return questions
    
def display_questions(questions: dict, question_num: int) -> str:
    '''takes in dictionary of questions, returns correct letter and answer'''
    # print question with html.unescape
    print(html.unescape(f"Question {question_num}: {questions[question_num]["question"]}"))
    correct_answer = questions[question_num]["correct_answer"]
    # if the question has 2 answer choices (True or False)
    if len(questions[question_num]["incorrect_answers"]) == 1:
        wrong_A = questions[question_num]["incorrect_answers"][0]
        answer_list = [correct_answer, wrong_A]
        # shuffles correct and incorrect answers
        random.shuffle(answer_list) 
        print(html.unescape(f"a. {answer_list[0]}"))
        print(html.unescape(f"b. {answer_list[1]}"))
        # checks which letter the right anwser corresponds with
        if correct_answer == answer_list[0]:
            correct_letter = "a"
        elif correct_answer == answer_list[1]:
            correct_letter = "b"
        # if the question has 4 answer options
    elif len(questions[question_num]["incorrect_answers"]) > 1:
        wrong_A = questions[question_num]["incorrect_answers"][0]
        wrong_B = questions[question_num]["incorrect_answers"][1]
        wrong_C = questions[question_num]["incorrect_answers"][2]
        answer_list = [correct_answer, wrong_A, wrong_B, wrong_C]
        # shuffles incorrect and correct anwser options
        random.shuffle(answer_list) 
        print(html.unescape(f"a. {answer_list[0]}"))
        print(html.unescape(f"b. {answer_list[1]}"))
        print(html.unescape(f"c. {answer_list[2]}"))
        print(html.unescape(f"d. {answer_list[3]}"))
        # checks which letter the right anwser corresponds with
        if correct_answer == answer_list[0]:
            correct_letter = "a"
        elif correct_answer == answer_list[1]:
            correct_letter = "b"
        elif correct_answer == answer_list[2]:
            correct_letter = "c"
        elif correct_answer == answer_list[3]:
            correct_letter = "d"
    
    return correct_letter, correct_answer


def check_correct(correct_letter: str, correct_answer: str, ladder_i: int) -> int:
    '''takes in correct letter and answer, returns user money amount after the user answers the question'''
    # if user gives a correct answer, advance up the ladder and move on to the next question
    # ladder_i = initial ladder value
    ladder = ladder_i    
    letter_choice = input(f"Type letter answer: ")
    # adds $100 when user gets a question right
    if correct_letter in letter_choice.lower():
        ladder += 100
        print("Correct!")
    else:
        # drops user down to a certain amount if a response is wrong
        print()
        print("Sorry, that was incorrect.")
        print(html.unescape(f"Correct answer is: {correct_letter}. {correct_answer}"))
        # between $0 and $200
        if ladder < 200:
            ladder = 0
        # below $400
        elif 400 > ladder >= 200:
            ladder = 200
        # below $600
        elif 600 > ladder >= 400:
            ladder = 400
        # below $800
        elif 800 > ladder >= 600:
            ladder = 600
        # below $1000
        elif 1000 > ladder >= 800:
            ladder = 800
    # displays money amount
    print(f"Your money: ${ladder}")
    print()
    print("-" * 20)
    return ladder
        

def main():    
    # gives instructions, sets accumulating variables to 0, and gets questions from the API
    gives_instructions()
    ladder_i = 0
    questions = get_questions()
    # asks 10 questions
    for i in range(1, 11):    
        letter, value = display_questions(questions, i)
        ladder_f = check_correct(letter, value, ladder_i)
        ladder_i = ladder_f
    # prints final player money winnings
    print(f"Good job! You got ${ladder_f}!")

main()