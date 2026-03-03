'''
Practice with using the Open Trivia Database
https://opentdb.com/
'''
import requests
import html

def main():
    # example of un-encoding html 
    print(html.unescape("Which greek mathematician ran through the streets of Syracuse naked while shouting &quot;Eureka&quot; after discovering the principle of displacement?"))

    # get the response from the API
    response = requests.get("https://opentdb.com/api.php?amount=10&category=19").json()
    
    response_code = response.get("response_code")
    results = response.get("results")

    # 0 means success!
    if response_code == 0:
        print(results[0]["question"])
        # TO DO: Print out the just the question for the first Q 
        # ask the user for input 
        # display the correct answer
    else:
        print("Oops try again.")

main()

















'''
Practice using the open trivia database
https://opentdb.com/
'''
'''
import requests
import html

def main():
    # demonstration of how to get rid of html encoding
    print(html.unescape("What type of function is x&sup2;+2x+1?"))

    # get the response from the API 
    response = requests.get("https://opentdb.com/api.php?amount=10&category=19").json()
    
    response_code = response.get("response_code")
    results = response.get("results")

    # response code of 0 means success!
    if response_code == 0:
        # print the first question
        print(results[0]["question"])
        user_ans = input("Your answer: ")
        print(results[0]["correct_answer"])

    else:
        print("Oops try again")

main()
'''