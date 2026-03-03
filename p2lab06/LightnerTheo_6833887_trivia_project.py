'''
Lab 06 1/23
Theo and Connor
Sports Trivia project
'''

import requests
import html
import random

def print_choices(correct_ans: str, wrong_ans: list) -> list:
    ''' Takes in correct choice and choices. Returns list of all choices for multiple choice questions'''
    choices = [correct_ans]
    letters = ["a","b","c","d"]

    for i in range(len(wrong_ans)):
        choices.append(wrong_ans[i])

    random.shuffle(choices)

    for i, item in enumerate(choices):
        print(f"{(letters[i])}) {html.unescape(item)}")
    
    return choices

def check_ans(user_ans: str, correct_ans: str, score: int, choices: list):
    '''purpose is to check if the user's answer is correct or not
     takes in user ans and correct ans, take in score'''
    

    #checking ans if user enters a letter
    letters = ["a", "b", "c", "d"]
    if user_ans.lower() in letters:
        user_ans = choices[letters.index(user_ans.lower())]

    if user_ans.lower() == correct_ans.lower() :
            print("\nYou are correct!")
            score += 1
                
    else:
        print("\nWrong.")
        print(f'The correct answer is: {correct_ans}')
    print("-" * 50)

    return score
            


def main():

    print()
    print("Welcome to our sports trivia game! \nYou will answer 15 multiple choice or true/false questions.\nGood luck! \n")


    #getting response from the api
    response = requests.get("https://opentdb.com/api.php?amount=15&category=21").json()

    response_code = response.get("response_code")
    results = response.get("results")

    score = 0
    if response_code == 0:

        for i in range (15):
            
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

            #get correct/incorrect answer each time
            correct_ans = html.unescape(results[i]["correct_answer"])
            wrong_ans = html.unescape(results[i]["incorrect_answers"])

            #print options
            choices = print_choices(correct_ans, wrong_ans)
            

            user_ans = input("Your answer: ")

            #calling check ans func and updating the core
            score = check_ans(user_ans, correct_ans, score, choices)
           
        
        print()
        print(f"Final score: {score}/15\n or {(score/15)*100:.0f}%")
    else:
        print("Server is busy, try again.")
        

main()