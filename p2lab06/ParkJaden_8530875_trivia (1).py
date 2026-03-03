'''
Trivia competition game
'''
import requests
import html
import random
import time

def instructions()-> int:
    '''gives instructions and figures out how many people are playing'''
     #instructions for coresponding player amounts
    duo_instructions = [ "Please get a friend to compete with.",
                    "You will take turns answering questions",
                    "Questions will get more difficult over time.",
                    "First person to get 3 questions wrong loses.",
                    "For multiple choice questions respond a,b,c,d of the corresponding answer",
                    "Have Fun!",              
    ]
    solo_instructions = ["You will keep answering questions until you get 3 wrong",
                         "Questions will get more difficult over time.",
                         "For multiple choice questions respond a,b,c,d of the corresponding answer",
                         "Have Fun!",             
    ]

    #giving a choice to play the game 1 or 1v1
    while True:
        try:
            player_amount = int(input("Please select 1 for solo-mode or 2 for two player: "))
            if player_amount == 1 or player_amount == 2:
                break
            print("Oops, please select 1 or 2")
        except ValueError:
            print("Oops, please select 1 or 2")
    
    #printing different instructions depending on who's playing
    if player_amount == 1:
        for sentance in solo_instructions:
            print(sentance)
            time.sleep(2)

    elif player_amount == 2:
        for sentance in duo_instructions:
            print(sentance)
            time.sleep(2)

    return player_amount

def get_questions(link: str)-> dict:
    '''returns the dictionary of the questions based on how many questions have been asked'''
    # while loop so it keeps trying to get the data until it gets it and doesn't crash
    while True:
        response = requests.get(link).json()
        response_code = response.get("response_code")

        #if the response code is not 0 it may crash so we want it to try again
        if response_code == 0:
            #we only need to results part since we already verified the response code
            quizbank = response["results"]
            return quizbank
        else:
            print("oops try again")

def whos_turn(questionsasked: int,p1wrong:int, p2wrong: int)-> bool:
    ''' takes in how many questions have been asked and returns whos turn it is'''
    if questionsasked % 2 != 0:
        print("")
        print(f"Player 2's turn, Player 2 has {p2wrong} wrong")
        return 2
    else:
        print("")
        print(f"Player 1's turn, Player 1 has {p1wrong} wrong")
        return 1

def ask_question(quizbank: dict, num: int)-> int: 
    ''' takes in the dictionary of questions and the amount of questions asked
        also asks the user for their answer and returns whether it was correct'''
    #open list for the to format the answer, question variable to not repeat code
    multi = []
    question = quizbank[num]
    print()
    print(html.unescape(question["question"]))

    #determinitng the type of question and asking the question in the right format
    if (question["type"]) == "multiple":
        answers = []
        # puting all the answers in a blank list and then shuffling
        choice_list = ["a","b","c","d"]
        correct = question["correct_answer"]
        for choice in question["incorrect_answers"]:
            answers.append(choice)
        answers.append(correct)
        random.shuffle(answers)

        #putting the answers in a nice format and allowing ther user to respond abcd
        print("Is it...")
        time.sleep(2)
        for postition, choice in enumerate(answers):
            print(f"{choice_list[postition].upper()}. {html.unescape(choice)}")
            time.sleep(.5)
        while True:
            answer = input("Answer: ")
            if answer.lower() in "abcd":
                break
            else:
                print("Oops, please respond a,b,c,d")

        answer = answers[choice_list.index(answer.lower())]

    #if it is a bool then easier 
    elif (question["type"]) == "boolean":
        correct = question["correct_answer"]
        time.sleep(1)
        while True:
            answer = input("True or False: ").lower().capitalize()
            if answer.lower() == "t":
                answer = "True"
                break
            elif answer.lower() == "f":
                answer = "False"
                break
            print("Oops please enter true, false, t, or f")

    #evaluating the answer and returning yes or no
    if correct != answer:
        print(f"Incorrect. the answer was {correct}.")
        return "no"
    else:
        print("Correct!")
        return "yes"

def update_score(p1wrong: int, p2wrong: int, player: int,)-> int:
    '''takes in the number each player got wrong and updates the correct user's score'''
    if player == 1:
        p1wrong +=1
    else:
        p2wrong +=1
    return p1wrong, p2wrong

def main():
    #saving the three links to the APIs
    easy_questions = "https://opentdb.com/api.php?amount=20&difficulty=easy"
    medium_questions = "https://opentdb.com/api.php?amount=20&difficulty=medium"
    hard_questions = "https://opentdb.com/api.php?amount=20&difficulty=hard"

    print("Welcome to Triva competition")
    p1wrong = 0
    p2wrong = 0

    player_amount = instructions()

    for i in range(100):
        #getting a new set of questions when both players have answered 3 of the level without losing
        if i == 0:
            results = get_questions(easy_questions)
            print("Easy Questions: ")
        elif i == 7:
            results = get_questions(medium_questions)
            print("Medium Questions: ")
        elif i == 13:
            results = get_questions(hard_questions)
            print("Hard Questions: ")
        else:
            pass
        time.sleep(1)

        #actual gameplay
        if player_amount == 1:
            print(f"You have {p1wrong} wrong")
            player = player_amount
        else:
            player = whos_turn(i,p1wrong,p2wrong)

        answer = ask_question(results, i)
        if answer == "no":
            p1wrong, p2wrong = update_score(p1wrong,p2wrong,player)
        
        #if one player has gotten more than three wrong then the game ends
        if p1wrong == 3 and player_amount == 1:
            print("You got 3 wrong, Game Over")
            print(f"Answered {i+1} questions total! Good job!")
            break
        elif p1wrong == 3:
            print("Game Over. P2 has won")
            break 
        if p2wrong == 3:
            print("Game Over. P1 has won")
            break
            
main()