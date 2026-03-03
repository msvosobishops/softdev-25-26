'''
Minh/Ari
Jeopardy-ish Trivia Game
'''
import requests
import random
import html
import time

def welcome():
    #welcome to user
    ''' no parameters, displays instructions and asks the user to press enter 
    to start, no return'''

    print()
    #colors - > https://www.geeksforgeeks.org/python/print-colors-python-terminal/

    input("Welcome to TRIPPY TRIVIA!\n\n"
        "\033[1mThis is a trivia game where you can answer questions of varying difficulty.\033[0m\n"
        "The harder the question is, the more points you can earn!\n\n"
        "\033[33mTry to earn 20 points or more, and don't go below -15 points!\033[0m\n"
        "You will have the option to stop whenever you would like.\n\n"
        "If you are stuck, you may answer with '50/50' to get 2 options.\n"
        "This will earn you half points if you are correct,\n"
        "but if you answer incorrectly, you will lose 2x the points!\n\n"
        "Press Enter to continue: ")
    
    print("\nYour current score is: 0")
    print()

def difficulty() -> int:

    '''no parameters, asks user for difficulty level, returns that level as an integer'''
    while True:
        
        
        diff = input("Which level difficulty would you like (1,2,3)? ")

        # checks if user entered a valid difficulty
        if diff not in ["1", "2", "3"]:
            print("\n !!!Please enter only 1, 2, or 3, for difficulty level!!!\n")
        else:
            return int(diff)
            
def access_api() -> tuple[int, list, int]:

    '''no parameters, uses the difficulty to generate a question with that
    difficulty from the API, and returns the response code, results(includes the question)
    and the difficulty'''

    diff = difficulty()

    if diff == 1:
        questions = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple").json()
    elif diff == 2:
        questions = requests.get("https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple").json()
    else:
        questions = requests.get("https://opentdb.com/api.php?amount=1&difficulty=hard&type=multiple").json()
    
    # accesses response code, and the results list of the dictionary that includes the question
    response_code = questions.get("response_code")
    results = questions.get("results")

    return response_code, results, diff

def generate_question() -> tuple[bool, bool, int] | None:

    # ^^^ multiple possible return types:
    # https://realpython.com/python-type-hints-multiple-types/
    
    '''no parameters, checks if the question (from the api)
    loaded properly, creates a scrambled list of answers, returns T/F if the 
    player answered correctly and if they used 50/50, and the difficulty'''

    # stores the response code, results, and difficulty that was returned from
    # the access_api function
    response_code, results, diff = access_api()
    choices = []
    
    #created a list of mulitple choices, adds correct/incorrect answers,
    # then scrambles the list
    try:
        answer = results[0]["correct_answer"]
    except TypeError:
        print("Please wait 5 seconds....")
    if response_code == 0:
        choices.append(answer)

        for i in range(3):
            choices.append(results[0]["incorrect_answers"][i])
        random.shuffle(choices)

        print(html.unescape(f"{results[0]['question']}"))

        for i in range(4):
            print()
            print(html.unescape(f"{i+1}) {choices[i]}"))
        print()

    # if the response code is not 0, asks user to try again
    else:
        print("The system encountered an error, please try again.")
        return None
    
    # finds the location of the correct answer in the list
    index = int(choices.index(answer)) + 1
    
    is_correct, used_5050 = check_answer(html.unescape(answer), index, choices)

    return is_correct, used_5050, diff
    
def check_answer(answer: str, index: int, choices: list) -> tuple[bool, bool]:

    '''takes in the answer to the question and its index(location) in the multiple
    choice options, and asks/checks if the user answers correctly, returns T/F 
    if correct'''

    user_answer = input("What is your answer? ")

    # check if user input is either the answer or the number option 
    
    used_5050 = False

    if user_answer.lower() == answer.lower() or str(index) == user_answer:
        print("\033[32mThat is correct!\033[0m")
        return True, used_5050
    
    elif user_answer == "50/50":
        #make it so that the user gets 2 choices instead of 4
        answer_50_50, new_index = fifty_fifty(answer, choices, index)
        used_5050 = True
        
        #check answer and return whether they answered correctly AND that they used 50/50
        if answer_50_50.lower() == answer.lower() or answer_50_50 == new_index:
            print("\033[32mThat is correct!\033[0m")
            return True, used_5050
        
        print(f"\033[31mThat is incorrect, the correct answer was ({index}) {answer}.\033[0m")
        return False, used_5050
    else:
        print(f"\033[31mThat is incorrect, the correct answer was ({index}) {answer}.\033[0m")
        return False, used_5050

def fifty_fifty(answer: str, choices: list, index) -> tuple[str, int]:

    '''takes in the correct answer, the whole list of choices, and the index
    of the correct answer, chooses 1 correct and 1 wrong answer to ask the user,
    returns the user's input and the index of the correct answer in the 50/50 list'''

    #making list of incorrect answers by taking out the correct answer from possible answers
    
    incorrect_answers = choices.copy()
    incorrect_answers.pop(index-1)
    #randomely choosing a wrong option for the 50/50
    wrong_option = random.choice(incorrect_answers)

    two_choices = []
    two_choices.append(wrong_option)
    two_choices.append(answer)
    random.shuffle(two_choices)
    
    while True:
        print("-"*36)
        # print two options
        user_input = input(f"\n1) {html.unescape(two_choices[0])}\n\n2) {html.unescape(two_choices[1])}\n\nWhat is your answer? ")
        
        #check if they answered 1/2, or one of the possible answer
        if user_input in ["1", "2"]:
            choice_index = int(user_input)-1
            return two_choices[choice_index], two_choices.index(answer)
        
        elif user_input.lower() == two_choices[0].lower() or user_input.lower() == two_choices[1].lower():
            return user_input, two_choices.index(answer)
        
        else:
            print("\nInvalid input. Please correctly type 1, 2, or the answer itself.")
            print("-"*54)

def calculate_points(is_correct: bool, used_5050: bool, diff: int,) -> float:

    '''takes in T/F whether user answered correctly and the difficulty of the question,
    calculates the amount of points that should be added (pos/neg) to the score 
    and returns that amount'''

    print()

    # returning the difficulty level to add to points if the user got the question correct
    # and halving if they used 50/50
    if is_correct == True and used_5050 == False:
        print(f"Points scored this question: {diff}")
        return diff
    
    elif is_correct == True and used_5050 == True:
        print(f"You scored half points for this question: +{diff/2}")
        points_5050 = diff/2
        return points_5050
    
    # returning the negative of the difficulty level to add to points if the user 
    # got the question wrong (depending if they used 50/50)
    elif used_5050 == True:
        print(f"You lost double points! -{diff*2}")
        points_5050 = diff*(-2)
        return points_5050
    
    else: 
        print(f"You lost {diff} points.")
        return (-1 * diff)
        
def main():

    welcome()
    score = 0
    
    while True:
        result = generate_question()

        # if the question does not load, cooldown for 5 seconds
        if result == None:
            time.sleep(5)
        else:
            is_correct, used_5050, diff = result
            
            # adding the calculated score to current score
            added_points = calculate_points(is_correct, used_5050, diff)
            score += added_points

            print(f"You have {score} points.")
            # win/losing
            if score >= 20:
                print("\033[1;32m!!!!! You Won !!!!!\033[0m")
                break
            elif score < -15:
                print("\033[1;31m!!!Sorry!!! You lost!!!\033[0m")
                break
            
            finished = input("Would you like to continue (y/n)? ")
            if "n" in finished.lower():
                break
    print(f"\n{'-'*10}GAME OVER{'-'*10}\n")
        
    print(f"Thanks for playing! \nYou had a total of {score} points.\n")
            
main()