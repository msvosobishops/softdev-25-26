'''
Lab 06 1/23
Theo and Connor
Trivia project
'''

import requests
import html
import random

def print_choices(correct_ans: str, wrong_answer: list) -> list:
    '''
    Return: nothing
    Parameters: correct choie and wrong choice
    Purpose: to print to the user 4 choices for an answer
    ''' 
    letters = ["a","b","c","d"]
    choices = [correct_ans]
    for i in range(len(wrong_answer)):
        choices.append(wrong_answer[i])
               
    random.shuffle(choices)

    for i, items in enumerate(choices):
        print(f"{letters[i]}) {html.unescape(items)}")

    print()
    
    return choices
            

def check_ans(user_ans: str, correct_ans: str, counter: int, choices: list):
    '''
    Return: N/A
    Parameters: The user choice and the correct answer, and how many questions they got right
    Purpose: to print if the user is correct or incorrect
    '''
    letters = ["a","b","c","d"]

    #Only if the user enters a letter, it would do the following to check
    if user_ans.lower() in letters:
        user_ans = choices[letters.index(user_ans.lower())]

    if user_ans.lower() == correct_ans.lower():
        print("You are correct!")
        counter += 1
        print("-"*50)
    else:
        print("Wrong.")
        print(f'The correct answer is: {correct_ans}')
        print("-"*50)
    return counter


def main():
    print("Welcome to our Trivia game! Please enter your answer with the correct answer, or choose a, b, c or d")
    print("You will answer 15 multiple choice/True or False questions. We will keep track of your score. Good Luck!")

    #getting response from the api
    response = requests.get("https://opentdb.com/api.php?amount=15&category=21").json()
    response_code = response.get("response_code")
    results = response.get("results")
    #_____________________________________________________________________________________

    if response_code == 0:
        counter = 0
        for i in range (15):
            #get correct/incorrect answer each time
            correct_ans = html.unescape(results[i]["correct_answer"])
            wrong_ans = html.unescape(results[i]["incorrect_answers"])
            
            #print question type
            if results[i]["type"] == "boolean":
                print()
                print("True/ False question:")
            else:
                print()
                print("Multiple Choice question:")
            

            #print questions
            question = results[i]["question"]
            print(html.unescape(question))

            #print choices and keep the answer choices
            questions_list = print_choices(correct_ans, wrong_ans)

            #Get user input
            user_ans = input("What is your answer: ")

            #Check user input
            counter = check_ans(user_ans, correct_ans, counter, questions_list)
            
    else:
        print("Server is busy, try again in 5 secs.")
        

    print(f"You got {counter}/15 questions  right! thats around {(counter/15)*100:.0f}%") 

    
main()