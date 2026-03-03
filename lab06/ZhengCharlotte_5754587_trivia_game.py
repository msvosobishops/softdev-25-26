'''
Cady and Charlotte
Who Wants to be a Millionare
*0, 100, 200, 300, 500, *1000, 2000, 4000, 8000, 16000, *25000, 50000, 100000, 250000,
500000, 1 million
5 easy questions, 5 medium questions, 5 hard questions
'''
import random
import requests
import html
    
def get_questions(results: list, i: int) -> tuple:
    '''takes in results from the questions and returns the correct (str) and 
    incorrect answers (list)'''
    
    # unescapes correct answer to get rid of symbols
    print(html.unescape(results[i]["question"]))
    correct_answer = html.unescape(results[i]["correct_answer"])
    
    # loops through incorrect answers and unescapes them
    incorrect_answer = results[i]["incorrect_answers"]
    incorrect_answers = []
    for ans in incorrect_answer:
        incorrect_answers.append(html.unescape(ans))
    
    return correct_answer, incorrect_answers


def generate_answers(correct_answer: str, incorrect_answers: list) -> list:
    '''takes in correct and incorrect answers and returns a randomized list of them'''
    
    # creates an empty list and adds the correct answer
    answer_choices = []
    answer_choices.append(correct_answer)

    # adds the incorrect answers
    # then randomly shuffles the list
    for j in range(3):
        answer_choices.append(incorrect_answers[j])
    random.shuffle(answer_choices) 

    return answer_choices


def get_user_answer(answer_choices: list) -> str:
    '''takes in answer choices, prints them out, and returns user's letter response'''
    
    # prints the answer choices and gets user input
    print(f"a. {answer_choices[0]}\nb. {answer_choices[1]}\nc. {answer_choices[2]}\nd. {answer_choices[3]}")
    print("-"*20)
    letter_response = input("Enter your response as 'a', 'b', 'c', or 'd' (q to leave): ")

    return letter_response


def check_for_error(letter_response: str, abcd: dict):
    '''takes in letter response and ensures that it is valid'''

    # asks for response until it is a proper input
    while letter_response not in abcd:
        print("Error. Must enter strictly 'a', 'b', 'c', or 'd', or 'q' to leave")
        letter_response = input("Enter your response: ")
    
    return letter_response
  
def convert_user_response(answer_choices: list, abcd: dict, letter_response: str) -> str:
    '''takes in answer choices, abcd, and letter response, and returns the user
    response in answer form'''
    
    # converts the user's response into answer form
    user_response = answer_choices[abcd.get(letter_response)]
    
    return user_response

def check_answer(user_response: str, correct_answer: str, money: int, question_number: int, user_money: int) -> tuple:
    '''takes in user response, correct answer, list of money, i, and user money, 
    checks if user response is correct, and returns new money amount (int) and 
    whether they can keep playing (bool)'''

    # if user is right, user money is raised and they can continue
    if user_response == correct_answer:
        user_money = money[question_number]
        print(f"Correct! Current money won: ${user_money}")
        print("-"*20)
        return user_money, True
    
    # if user is wrong, user money is decreased and they must leave
    else:
        if user_money < 1000:
            user_money = 0
        elif user_money >= 25000:
            user_money = 25000
        else:
            user_money = 1000

        print(f"Incorrect. The answer was {correct_answer}. Money won: ${user_money}")
        return user_money, False


def main():

    print("Welcome to Who Wants to be a Millionaire! There will be 15 questions, " \
    "each one you answer correctly, your possible winnings increases. If you get " \
    "one wrong, you will drop back to $0, $1000, or $25,000, depending on how far " \
    "you are, and you must leave. The level of difficulty of the questions " \
    "increases everytime five questions are answered. You have the choice to "  \
    "walk away whenever. ")
    print("-"*20)
    
    # creates a list of question difficulties
    difficulties = ["easy", "medium", "hard"]

    # creates a list of the money that can be earned
    money = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 
            25000, 50000, 100000, 250000, 500000, 1000000]
    
    # corresponds a, b, c, d, with a number and q with quit
    abcd = {"a": 0, "b": 1, "c": 2, "d": 3, "q": "quit"}

    # sets variables for question number and user money to keep track
    question_number = 0
    user_money = 0

    # loops through each difficulty
    for difficulty in difficulties:

        # gets the first 5 questions, response code, and results
        response = requests.get(f"https://opentdb.com/api.php?amount=5&difficulty={difficulty}&type=multiple").json()
        response_code = response.get("response_code")
        results = response.get("results")

        # continues if the response code is 0
        if response_code == 0:
            for i in range(5):    
                # gets five questions and the correct and incorrect answers for each
                correct_answer, incorrect_answers = get_questions(results, i)
                
                # creates an empty list and adds the correct answer
                answer_choices = generate_answers(correct_answer, incorrect_answers)

                # prints the answer choices and gets user input
                letter_response = get_user_answer(answer_choices)
                print("-"*20)
            
                # ensuring the a proper input
                letter_response = check_for_error(letter_response, abcd)
        
                # ends the program if user input is q
                if letter_response == "q":
                    print(f"You have chosen to walk away. Money won: ${user_money}")
                    return

                # converts the user's response into answer form
                user_response = convert_user_response(answer_choices, abcd, letter_response)

                # updates user money based on whether correct
                user_money, keep_playing = check_answer(user_response, correct_answer, money, question_number, user_money)
                if keep_playing == False:
                    return
                
                # adds one to the question number
                question_number += 1
                
        else:
            print(f"Error. Could not get {difficulty} questions. Try again.")


main()