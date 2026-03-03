'''
emma wang & alice zhu
1/23/2026 
create a trivia game! 
''' 

# import built-in libraries we will use
import time 
import requests 
import html 
import random

def game_tutorial(): 
    '''prints instructions about how to play the trivia game'''
    # shows tutorial and instructions
    print("IN THIS GAME, THERE WILL BE QUESTIONS TESTING YOUR GENERAL KNOWLEDGE. ")
    time.sleep(2)  # wait 2 seconds before showing next line
    print("THERE ARE 3 DIFFICULTIES, EASY, MEDIUM, AND HARD, WORTH 10, 20, AND 30 POINTS RESPECTIVELY")
    time.sleep(3.5)
    print("THERE WILL BE 5 QUESTIONS IN EACH DIFFICULTY LEVEL. IF YOU GET MORE THAN 120 POINTS, YOU WIN!")
    time.sleep(3.5)
    print("ONCE THE BOARD PRINTS, YOU WILL ENTER ONE OF THE NUMBER SHOWN UNDER EASY, MEDIUM, OR HARD")
    time.sleep(3.5)
    print('IF YOU WANT TO QUIT THE PROGRAM, TYPE IN A "Q"')
    time.sleep(2)
    print("GOOD LUCK AND HAVE FUN!")
    time.sleep(1)


def get_questions()-> list: 
    '''get questions from the API, ensures that there's 5 easy 5 medium and 5 hard, and returns the list of questions'''
    # loop to get questions until there's 5 in each difficulty
    while True:
        # loop to call the API until a success
        while True: 
            ## call the API for 50 multiple-choice questions
            response = requests.get("https://opentdb.com/api.php?amount=50&category=9&type=multiple").json()
        
            response_code = response.get("response_code")
            results = response.get("results")

            #if API works, return the results 
            if response_code == 0: 
                break 
            # API failed, wait and try again
            else: 
                print("working on it...wait 5 seconds")
                time.sleep(5)

        # sort the questions 
        easy, medium, hard = sort_questions(results)

        if len(easy) >= 5 and len(medium) >= 5 and len(hard) >= 5:
            q_list = easy[:5] + medium[:5] + hard[:5]
            return q_list

def sort_questions(results:list) -> tuple:
    '''sort the questions from the API into easy, medium, and hard, return these lists'''
    easy_questions = []
    medium_questions = []
    hard_questions = []

    #sort questions into easy, medium, and hard
    for question in results: # go through each question
        if question["difficulty"] == "easy": 
            easy_questions.append(question)
        elif question["difficulty"] == "medium": 
            medium_questions.append(question)
        else: 
            hard_questions.append(question)

    #  return three lists
    return easy_questions, medium_questions, hard_questions
    
def print_board(pos): 
    """Print the game board showing positions for each difficulty level."""

    print("    GENERAL KNOWLEDGE:")
    print("  EASY  | MEDIUM  |   HARD   ")
    print("-----------------------------")
    # show 5 rows of numbers for each difficulty
    print(f"   {pos[0]}    |    {pos[5]}    |    {pos[10]}")
    print(f"   {pos[1]}    |    {pos[6]}    |    {pos[11]}")
    print(f"   {pos[2]}    |    {pos[7]}    |    {pos[12]}")
    print(f"   {pos[3]}    |    {pos[8]}    |    {pos[13]}")
    print(f"   {pos[4]}    |    {pos[9]}   |    {pos[14]}")

def get_move(q_list: list)->tuple:
    """Prompt the user to pick a question number or quit the game."""
    
    while True:
        user_num = input("pick a number (1-15) or Q to quit: ")

        # user wants to quit
        if user_num == "Q":
            return "Q" 

        # not a number
        if not user_num.isdigit():
            print("Please enter a number or Q.")
            continue

        # convert input to int
        num = int(user_num)

        if num < 1 or num > 15:
            print("That's not a valid position, try again.")
        else:
            return num

def get_question(q_list: list,num: int)->tuple:
    """Return the question, shuffled answers, correct answer index, and difficulty."""
    question = q_list[num - 1]["question"]
    correct_answer = q_list[num-1]["correct_answer"]
    # copy incorrect answers
    answer_lst = q_list[num-1]["incorrect_answers"].copy()
    # add correct answer
    answer_lst.append(correct_answer) 
    # shuffle all answers so correct one is random
    random.shuffle(answer_lst) 
    correct_index = answer_lst.index(correct_answer)
    difficulty_level = q_list[num-1]["difficulty"]
    return question, correct_index, answer_lst, difficulty_level

def main():
    """Run the trivia game, handle user input, scoring, and display results."""

    print("WELCOME TO TRIVIA!")
    time.sleep(1)
    #Ask user if they want a tutorial
    while True: 
        tutorial = input("Would you like a tutorial on this game(Y/N) ")
        if tutorial == "N".lower(): 
            break 
        elif tutorial == "Y".lower(): 
            game_tutorial()
            break 
        else: 
            print("Oops! pick either Y or N to begin")

    # initialize board numbers
    pos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # keep track of already chosen 
    player_board_pos = []
    print_board(pos)
    # get questions from API
    q_list = get_questions()
    
    # start with 0 points
    points = 0

    # 15 questions in total
    for i in range(15):
        user_move = get_move(q_list)

        # if user quits
        if user_move == "Q":
            print("YOU HAVE QUIT THE PROGRAM.")
            break

        # Make sure user picks a position not already chosen
        while True:
            if user_move not in player_board_pos: 
                # mark this position as used
                player_board_pos.append(user_move)
                break
            else:
                print("OOPS, YOU ALREADY WENT THERE.")
                time.sleep(1)
                print(f"THESE ARE THE POSITIONS OF THE PLACES YOU HAVE ALREADY MOVED. {player_board_pos}")
                time.sleep(2)
                # lets the player pick another position
                print("PLEASE PICK A DIFFERENT LOCATION")
                user_move = get_move(q_list)

        question, correct_index, shuffled_answers, difficulty_level = get_question(q_list, user_move)
        print(html.unescape(question))
        time.sleep(1)
        # show all four answer choices
        print(html.unescape(f"1. {shuffled_answers[0]} 2. {shuffled_answers[1]} 3. {shuffled_answers[2]} 4. {shuffled_answers[3]}"))
        time.sleep(1)

        # Loop until user gives valid answer
        while True:
            user_answer = input("YOUR ANSWER (1,2,3,4) or Q to quit: ")

            # quit
            if user_answer == "Q":
                print("YOU HAVE QUIT THE PROGRAM.")
                return

            # not a number
            if not user_answer.isdigit():
                print("OOPS! THATS NOT AN ANSWER CHOICE. PLEASE ENTER 1,2,3, OR 4")
                continue

            # make it an int
            user_answer = int(user_answer)

            # invalid number
            if user_answer not in [1,2,3,4]:
                print("OOPS! THATS NOT AN ANSWER CHOICE. PLEASE ENTER 1,2,3, OR 4")

            # correct answer
            elif user_answer == correct_index + 1:
                print("CONGRATS! YOU GOT THAT QUESTION RIGHT!")
                time.sleep(0.5)

                # add points based on difficulty
                if difficulty_level == "easy":
                    # 10 points if easy
                    points += 10
                elif difficulty_level == "medium":
                    # 20 points for medium
                    points += 20
                else:
                    # 30 points for hard
                    points += 30

                print(f"CURRENT POINTS: {points}")
                time.sleep(1)
                break

            # wrong answer
            else:
                print(
                    f"UNFORTUNATELY, YOU GOT THAT QUESTION WRONG. "
                    f"THE CORRECT ANSWER WAS {correct_index + 1}: "
                    f"{shuffled_answers[correct_index]}"
                )
                time.sleep(1)
                print(f"CURRENT POINTS: {points}")
                time.sleep(1)
                break
    
        # mark board position as used with an X
        pos[user_move - 1] = "X"
        print_board(pos)

    # End of game
    time.sleep(1)
    print(f"YOUR TOTAL POINTS FOR THIS ROUND WAS {points}")
    time.sleep(1)
    # win = 120 points
    if points >= 120: 
        print("YAY! YOU HAD MORE THAN 120 POINTS. CONGRATS!")
        time.sleep(1)
    else: 
        print("YOU MAY NOT HAVE GOTTEN OVER 120 POINTS THIS TIME, BUT YOU CAN TRY AGAIN NEXT TIME")
        time.sleep(1)

    print("PLEASE PLAY AGAIN!")
    
main()