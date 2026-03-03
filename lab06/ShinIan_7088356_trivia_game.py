'''
Ian and Jonah, Who wants to Be a Millionare
Lab 06 - Trivia Game

'''

import requests
import html
import time
import random

money = ["100", "200", "300", "500", "1,000", "2,000", "4,000", "8,000", "16,000", "32,000", "64,000", "125,000", "250,000", "500,000", "1,000,000"]

def ask_question(results: list) -> int:
    '''takes in the questions formed by get_questions, asks the user the questions and returns the money they win'''
    
    win_counter = 0
    for i in range(15):
        if win_counter == 15:
            return 1000000
        answer_choices = []
        correct = results[i]["correct_answer"]
        incorrect = results[i]["incorrect_answers"]
        print(html.unescape(results[i]["question"]))
        for i in range(3):
            answer_choices.append(incorrect[i])
        answer_choices.append(correct)
        random.shuffle(answer_choices)
        abcd = ["a", "b", "c", "d"]
        for i in range(4):
            print(html.unescape(f"{abcd[i]}) {answer_choices[i]}"))
        while True:
            user_answer = input("Enter your answer: ")
            if user_answer.lower() not in abcd:
                print("Please enter your answer as one of the letter answer choices!")
                print()
            else:
                break
        answer_index = abcd.index(user_answer)
        correct_answer_index = answer_choices.index(correct)
        
        if answer_index == correct_answer_index:
            time.sleep(0.5)
            print()
            print("Correct!")
            
            win_counter +=1
            
            if win_counter == 15:
                return 1000000
            
            while True:
                print()
                leave = input(f"Would you like to cash out now and take home ${money[win_counter-1]}? ")
                if leave.lower() == "yes":
                    return money[win_counter-1]
                if leave.lower() == "no":
                    break
                else:
                    print("Please enter your answer as a yes or a no.")
            
        else:
            time.sleep(0.5)
            print("incorrect!")
            print(html.unescape(f"the correct answer is: {correct} "))
            print("-"*40)
            if win_counter <= 4:
                return 0
            if win_counter <=9:
                return 1000
            if win_counter <=14:
                return 32000
            
        time.sleep(0.5)
        print("-"*40)


def gameplay():
    '''intro print statements'''
    print("Today we will be playing Who Wants to Be Millionare!!!")
    time.sleep(0.8)
    print("The host today is Jonah Iancovici")
    time.sleep(0.8)
    print("Each question will move up in money value until it reaches the big 1 million!")
    time.sleep(0.8)
    print("Feel free to cash out whenever and take home your hard earned cash")
    time.sleep(0.8)
    print("Warning: if you get a question wrong, you will go down to the last jackpot you hit. " )
    time.sleep(0.8)
    print("JACKPOTS AT 1,000, 32,000, and 1,000,000")
    time.sleep(0.8)
    print("When entering an answer, type in the letter of your choice.")
    print("-"*40)

def endgame(money_won):
    '''conclusion, takes in how much money won and prints the user's winning'''
    if money_won == 1000000:
        print("CONGRATULATIONS YOU WON THE LARGEST JACKPOT!!!")
    else:
        print("Thank you for playing, Who Wants to be a Millionare!")
        print(f"After today's round you will be taking home a grand total of ${money_won}")
        print("Great try!")
    


def get_questions():
    
    '''calls api until successful and forms questions into a list'''
    while True:
        
        response = requests.get("https://opentdb.com/api.php?amount=15&category=9&difficulty=medium&type=multiple").json()

        response_code = response.get("response_code")
        results = response.get("results")
        if response_code ==0:
            return results
        time.sleep(4)
        
       




def main():
   
    gameplay() 
    questions = get_questions()
    money_won = ask_question(questions)
    endgame(money_won)

main()