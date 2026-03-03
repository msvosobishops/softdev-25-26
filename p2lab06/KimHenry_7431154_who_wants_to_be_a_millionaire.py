'''
Henry Kim and Michael Lu
1-23-2025
Who wants to be a millionaire
'''

#imports

import requests

import html

import random

def get_uguess(results: list) -> str:
    '''
    To get the users answer
    Results -> list
    Returns the user answer
    '''
    user_ans = input("Your answer: ").lower()
    #print lines to make it look good
    print("-"*40)
    return user_ans

def check_uans(uans: str, results: list, qnum: int)-> bool:
    '''
    To determine if the answer is right or wrong
    uans -> string, results-> list, qnum -> int
    Returns if the answer is right or wrong. 
    '''

    #list to store money progression

    money = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    #check if user answer matches correct answer and return true or false

    if uans.lower() == results[qnum]["correct_answer"].lower():

        print(f"Correct! You have ${money[qnum]}. ")
        return True

    else:

        return False

def play_game(results: list):
    '''
    The gameplay (questions, answers, saftey nets, money, etc)
    results -> list
    No returns, only prints things
    '''

    #store money progression

    money = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    #counter for answers correct in a row

    answers_correct = 0

    #loop for questions and nums
    for i in range(15):

        #Print the question

        print(html.unescape(results[i]["question"]))

        #print lines to make it look good

        for char in results[i]["question"]:
            print("-", end="")
        print("")

        #Counter for total answers

        tanswers = []

        #append and shuffle all of the answers in the list

        tanswers.append(results[i]["correct_answer"])
        for item in results[i]["incorrect_answers"]:
            tanswers.append(item)
        random.shuffle(tanswers)

        #print answers

        for item in tanswers:
            print(html.unescape(item))

        #run program to get the user guess

        answer = get_uguess(results)

        #Run program to check if it's right or wrong

        correctornot = check_uans(answer, results, i)

        #If they get a question wrong

        if correctornot == False:

            #If they get a question wrong but they have the $1000 saftey net

            if 5 < answers_correct < 10:
                print("You lost! But you still get $1000! ")
                print(html.unescape(f"The correct answer was {results[i]['correct_answer']}"))

            #If they get a question wrong but they have the $32000 saftey net

            if 10 < answers_correct < 15:
                print("You lost! But you still get $32000! ")
                print(html.unescape(f"The correct answer was {results[i]['correct_answer']}"))

            #If they get a question wrong without any saftey net

            else:
                print("Better luck next time!")
                print(html.unescape(f"The correct answer was {results[i]['correct_answer']}"))
                break

        #if they get a quesiton right

        elif correctornot == True:

            #ask user if they want to walk away with the money they have earned so far

            keep_going = input(html.unescape(f"Do you want to walk away now with ${money[i]}? "))

            #if they choose to walk away then break the loop

            if keep_going.lower() == "yes":
                print(html.unescape(f"You have just walked away with ${money[i]}. "))
                break

            #if they choose to keep going then go to the next question (run the loop again)

            else:
                print("Next question...")
                answers_correct += 1


        #if they get all 15 questions right

        if answers_correct == 15:
            print("Congratulations! You are a millionaire! ")

def main():

    #Get questions and answers from open trivia api

    response = requests.get("https://opentdb.com/api.php?amount=15").json()
    response_code = response.get("response_code")
    results = response.get("results")

    #Check if we got any results from open trivia api

    if response_code == 0:
        print("Welcome to Who wants to be amillionaire! You will answer fifteen random trivia questions getting more money for each correct answer. ")
        print("After you get five questions right, you will have a $1000 saftey net in case you get a question wrong. ")
        print("After you get ten questions right, you will have a $32000 saftey net in case you get a question wrong. ")
        play_game(results)
        
    else:

        print("Oops try again")

main()