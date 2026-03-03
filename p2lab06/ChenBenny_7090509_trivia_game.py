'''
Benny and Ashali
Trivia Game
1/23/2026
'''

import requests
import html
import time
from colorama import Fore, Back, Style #https://www.geeksforgeeks.org/python/print-colors-python-terminal/

def intro():
    '''intro print statements, no parameters or returns'''

    # prints introduction
    print(Fore.YELLOW + "Hello and welcome to Fortune Finders!" + Style.RESET_ALL)
    print()
    time.sleep(2)

    print("At the start of each round, you will be given the choice to get a question or leave the game. ")
    print("If you choose to get a question, you will be given a true or false question about a random subject.")
    print("If you choose to leave the game, the game will be over and you will leave with all the money you have earned.")
    print()
    time.sleep(2)

    print("Answering correctly will earn you money and allow you to begin another round.")
    print("The most money you can earn is $100,000,000 from answering 12 questions correctly.")
    print()
    time.sleep(2)

    print("If you answer a question incorrectly, you will automatically get saved.")
    print()
    time.sleep(2)
    
    print("You have a total of 3 saves.")
    print("After using a save, the question you got wrong will be skipped and you will be able to continue the game. ")
    print("You will not gain money from a save.")
    print()
    time.sleep(2)

    print("However, beware! If you run out of saves, then you will automatically lose the game and earn nothing.")
    print()
    time.sleep(2)

    print("The progression of the money is as follows:")
    print("$1000, $5000, $10000, $25000, $50000, $100000, $250000, $500000, $1000000, $5000000, $10000000, $100000000")
    print()
    time.sleep(2)

def get_question(question_number: int, questions: list) -> bool:
    '''Gets a question from questions list based on question number, 
       takes in the question number and questions list, 
       returns True or False'''

    #gets question from the list based on question number
    q = questions[question_number]

    print(html.unescape(q.get("question")) + " (True or False)") #prints the question from list
    user_ans = input("Your answer: ") #takes user input for answer


    if user_ans.lower() == html.unescape(q.get("correct_answer")).lower(): #checks if answer was correct
        print()
        print(Fore.GREEN + "Correct!" + Style.RESET_ALL) #from import function, source at top
        return True #returns True if correct answer

    else:
        print()
        print(Fore.RED + "Incorrect!" + Style.RESET_ALL) #from import function, source at top
        correct_answer = html.unescape(q.get("correct_answer")) 
        print(f"The correct answer is {correct_answer}") #prints the correct answer
        print()
        return False #returns false if incorrect answer



def score_tracker():
    '''Get questions from API, tracks money and question number, no parameters or returns'''

    response = requests.get("https://opentdb.com/api.php?amount=15&type=boolean").json() #gets response from API
    
    response_code = response.get("response_code") #sees if response was successful
    questions = response.get("results") #creates questions list that has all questions from API response

    if response_code != 0: #this means it was not successful
        print(Fore.RED + "Oops sorry! Questions didn't load. Please wait a while. Thank you!" + Style.RESET_ALL) #from import function, source at top
        print()
        return

    money_list = ["1,000", "5,000", "10,000", "25,000", "50,000", "100,000", 
                  "250,000", "500,000", "1,000,000", "5,000,000", "10,000,000", "100,000,000"] #money progression list

    #variables keeping track of user money and questions
    current_money = 0

    correct_counter = -1

    question_number = -1

    save = 3

    #loop that continues asking questions and saves
    while True:

        #checks to see if the user is on the last question and has won the game
        if question_number >= 11 and save == 3:
            print(Fore.YELLOW + "You've answered all the questions correctly! Congratulations!" + Style.RESET_ALL) #from import function, source at top
            print(f"{Fore.YELLOW}You are walking away with ${current_money}{Style.RESET_ALL}")
            print()
            break

        elif question_number >= 12 and save ==2:
            print(Fore.YELLOW + "You've answered all the questions correctly! Congratulations!" + Style.RESET_ALL) #from import function, source at top
            print(f"{Fore.YELLOW}You are walking away with ${current_money}{Style.RESET_ALL}")
            print()
            break

        elif question_number >= 13 and save == 1:
            print(Fore.YELLOW + "You've answered all the questions correctly! Congratulations!" + Style.RESET_ALL) #from import function, source at top
            print(f"{Fore.YELLOW}You are walking away with ${current_money}{Style.RESET_ALL}")
            print()
            break

        elif question_number == 14 and save == 0:
            print(Fore.YELLOW + "You've answered all the questions correctly! Congratulations!" + Style.RESET_ALL) #from import function, source at top
            print(f"{Fore.YELLOW}You are walking away with ${current_money}{Style.RESET_ALL}")
            print()
            break

        elif save != 0:
            #if not won game, asks user if they want a question or to leave
            print(f"{Fore.YELLOW}Right now, you can walk away with ${current_money} if you choose to leave on the next question.{Style.RESET_ALL}")
            print()
            choice = input("Do you want question or do you want to leave with what you have? (question or leave) ")

        #runs if they want a question
        if choice.lower() == "question":
            question_number += 1
            print()
            result = get_question(question_number, questions) #calls get_question function

        #this runs if they say anything other than question
        else:
            print() 
            print(f"{Fore.YELLOW}Thanks for playing! You are walking away with ${current_money}!{Style.RESET_ALL}") #from import function, source at top
            break

        #checks to see if they got the right answer
        if result == True:
            correct_counter += 1
            current_money = money_list[correct_counter]
            print(Fore.GREEN + "You have just won some money!" + Style.RESET_ALL) #from import function, source at top
            print()

        #runs if the user is on their last save
        elif result == False and save == 1:
            print(Fore.RED + "You have run out of saves, which means you have lost all your money." + Style.RESET_ALL)
            print(Fore.RED + "Unfortunately, the game is over." + Style.RESET_ALL) #from import function, source at top
            print()
            print(Fore.YELLOW + "Sorry, and good luck next time!" + Style.RESET_ALL)
            break

        #runs if use is not on their last save
        elif result == False and save > 1:
            save -= 1
            print(f"{Fore.GREEN}You have been saved! You have {save}/3 saves left.{Style.RESET_ALL}") #from import function, source at top
            print()

        #runs if they choose to leave the game
        else:
            print(Fore.RED + "Unfortunately, the game is over." + Style.RESET_ALL) #from import function, source at top
            print()
            print(f"{Fore.GREEN}However, in this round, you won {current_money}!{Style.RESET_ALL}") #from import function, source at top
            break

            


def main():
    
    intro()

    score_tracker()

main()