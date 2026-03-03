'''
Daniel Li
1-24-2026
Uses Open Triva Database for a game of jeopard, but all questions are worth the same
Parts:
displays grid of answer choices
asks the questions
keeps score
play against 1-3 bots

'''
import html
import requests
import time
import random
from inputimeout import inputimeout, TimeoutOccurred
import os

def word_rounding(word1: str, word2: str) -> bool:
    '''
    checks if two words are close enough and returns True false
    '''
    if len(word2) >= int(len(word1)*.5) and len(word2) <= int(len(word1)*1.25):
        # create letter index
        letter = 0
        # create correct letters
        correct = 0
        if len(word2) > len(word1):
            for char in word1:
                if char == word2[letter]:
                    correct += 1
                elif word2.find(char) != -1 and (char == word2[letter+1] or char == word2[letter-1]):
                    correct += .5
                elif char == word2[letter-1]:
                    correct += .5
                letter += 1
        else:
            for char in word2:
                if char == word1[letter]:
                    correct += 1
                elif word1.find(char) != -1 and (char == word1[letter+1] or char == word1[letter-1]):
                    correct += .5
                elif char == word2[letter-1]:
                    correct += .5
                letter += 1
        # check correctness
        if correct / len(word1) > .7:
            return True
        else: 
            return False
    else:
        return False
            
            




def settup_board() -> tuple[str, int, list]:
    '''
    sets up the board based on user preference
    bots, board randomization, game difficultly
    '''
    # find number of bots
    num_bots = 0
    while True:
        num_bots = input("How many bots do you want to play against: ")
        if num_bots == '1' or num_bots == '2' or num_bots == '3':
            break
        print("Invalid input")

    # find bot difficultly setting
    bot_difficulty = ''
    while True:
        bot_difficulty = input("What bot difficulty do you want(easy, med, hard): ").lower()
        if word_rounding('easy',bot_difficulty):
            bot_difficulty = 'easy'
            break 
        elif word_rounding('med',bot_difficulty):
            bot_difficulty = 'medium'
            break
        elif word_rounding('hard',bot_difficulty):
            bot_difficulty = 'hard'
            break
        print("Invalid input")
        #find game difficultly setting
    game_difficulty = ''
    while True:
        game_difficulty = input("What game difficulty do you want(easy, hard): ").lower()
        if word_rounding('easy',game_difficulty):
            game_difficulty = 'easy'
            break 
        elif word_rounding('hard',game_difficulty):
            game_difficulty = 'hard'
            break
        print("Invalid input")
    
    # create list of possible subjects and chose 5
    subject_choices = {"General Knowledge":9,
                       "Entertainment: Music":12,
                       "Entertainment: Video Games":15,
                       "Geography":22,
                       "History":23,
                       "Mythology":20,
                       "Politics":24,
                       "Science &amp; Nature":17,
                       "Entertainment: Books":10,
                       "Entertainment: Film":11}
    temp_board_catagories = [9,12,15,22,23,20,24,17,10,11]
    random.shuffle(temp_board_catagories)
    board_catagories = temp_board_catagories[:5]

    # make questions list
    questions = [[],[],[],[],[]]
    # make catagories list
    catagories = []
    # make correct answer list
    correct_answers = [[],[],[],[],[]]
    # make incorrect answer list
    incorrect_answers = [[],[],[],[],[]]

    # make counter
    i = 0
    for catagory in board_catagories:
        # generate link to api for columns
        link = f'https://opentdb.com/api.php?amount=3&category={catagory}&difficulty=medium&type=multiple'
        while True:
            # get the response from api
            response = requests.get(link).json()

            # get the response code to keep checking
            if response.get('response_code') == 0:
                # add to questions
                i += 1
                for j in range(3):
                    questions[i-1].append(html.unescape(response['results'][j]['question']))

                # add to catagories
                catagories.append(html.unescape(response['results'][0]['category']))

                # add to correct answers
                for j in range(3):
                    correct_answers[i-1].append(html.unescape(response['results'][j]['correct_answer']))
                # add to incorrect answers
                for j in range(3):
                    # loop over to create a new converted list
                    temp_list = []
                    for str in response['results'][j]['incorrect_answers']:
                        temp_list.append(html.unescape(str))
                    incorrect_answers[i-1].append(temp_list)
                break
            time.sleep(1)
            print('loading...')

    # set up dimensions
    board_width = 24 
    for string in catagories:
        board_width += len(string)


    return (num_bots, bot_difficulty, game_difficulty, board_width, catagories, 
            questions, correct_answers, incorrect_answers)


def print_game_board(num_bots: int, catagories: list, board_width: int, 
                     values: list, score: list):
    '''
    prints game board to the terminal based on bots #
    4 difficulties: easy, med, hard, rand
    5 catagories: random
    teams on the bottom
    '''
    # wait then clear terminal
    time.sleep(3)
    _ = os.system('clear')
    
    # setup box size between numbers based on the longest catagory name
    box_size = 0
    for string in catagories:
        if len(string) > box_size:
            box_size = len(string)
    box_size = box_size + 4
    # set up horizontal line
    horizontal_line = "-" * (box_size * 5 + 6)
    print(horizontal_line)

    # set up row variable
    row = ''
    # make and print catagory row
    for i in range(5):
        row += f'|{catagories[i]:^{box_size}}'
    row += '|'
    # print catagory row and reset
    print(row)
    row = ''
    print(horizontal_line)
    

    # print next rows
    for i in range(3):
        for j in range(5):
            row += f'|{values[j][i]:^{box_size}}'
        row += '|'
        print(row)
        row = ''
        print(horizontal_line)

    # print labels
    row = ''
    row += f"|{'player:':^{box_size}}"
    for i in range(len(score)-1):
        row += f"|{'bot'+str(i+1) + ':':^{box_size}}"
    row += '|'
    print(row)

    row = ''
    # print scores
    # make and print catagory row
    for i in range(len(score)):
        row += f'|{score[i]:^{box_size}}'
    row += '|'
    # print catagory row
    print(row)



def new_turn(num_bots: int, bot_difficulty: str, game_difficulty: str, 
                catagories: list, questions: list, correct_answers: list, 
                incorrect_answers: list, score: list, values: list, is_player: bool):
    '''
    the a new turn where they choose a question, and they fight to answer, 
    and returns the new score
    '''
    # only ask for user choice if  his turn
    if is_player == True:
        while True:
            while True:
                topic_choice = input("Player, choose a topic: ")
                if word_rounding(catagories[0].lower(), topic_choice):
                    topic_choice = catagories[0]
                    break
                elif word_rounding(catagories[1].lower(), topic_choice):
                    topic_choice = catagories[1]
                    break
                elif word_rounding(catagories[2].lower(), topic_choice):
                    topic_choice = catagories[2]
                    break
                elif word_rounding(catagories[3].lower(), topic_choice):
                    topic_choice = catagories[3]
                    break
                elif word_rounding(catagories[4].lower(), topic_choice):
                    topic_choice = catagories[4]
                    break
                else:
                    print("invalid input")
                    
            while True:
                value_choice = input("Player, choose a value: ")
                if value_choice != '100' and value_choice != '200' and value_choice != '300':
                    print("invalid input")
                else:
                    break
            if values[catagories.index(topic_choice)][int(value_choice) // 100 - 1] == 0:
                print("That question has already been asked")
            else:
                break
    else:
        # choose random catagory
        while True:
            topic_choice = random.choice(catagories)
            value_choice = random.choice([100,200,300])
            if values[catagories.index(topic_choice)][int(value_choice) // 100 - 1] == 0:
                pass
            else:
                break
        print("A bot has chosen a question")

    # countdown for question
    for i in range(3):
        print(f"Question in {3-i}")
        time.sleep(1)
    # set up x and y values
    x = catagories.index(topic_choice)
    y = int(value_choice) // 100 - 1
    print(questions[x][y])

    buzz = None
    # set up bot stats
    if bot_difficulty == 'easy':
        bot_buzz_time = random.randint(60,100) / 10
        num = 60
    elif bot_difficulty == 'med':
        bot_buzz_time = random.randint(40,60) / 10
        num = 75
    else:
        bot_buzz_time = random.randint(20,35) / 10
        num = 90
    # check if easy or hard difficulty: if easy, give multiple choice
    if game_difficulty == "easy":

        # set up multiple choice list
        abcd = ['a','b','c','d']
        answer_choices = [correct_answers[x][y]] + incorrect_answers[x][y]
        random.shuffle(answer_choices)
        for i in range(4):
            print(f'{abcd[i]}. {answer_choices[i]}')

        # Attempt to get user input with a timeout that represents the bots pressing
        
        try:
            buzz = inputimeout(prompt='buzz?', timeout=bot_buzz_time)

        except TimeoutOccurred:
            pass

        # if bots press first
        if buzz == None:
            if random.randint(1,100) <= num:
                # chose a random bot index and give them the score
                index = random.randint(1,len(score)-1)
                score[index] += values[x][y]
                values[x][y] = 0
                print(f"bot{index} buzzed after {bot_buzz_time} seconds and ",
                      f"answered correctly: {correct_answers[x][y]}")
            else:
                # chose a random bot index and subtract the score
                index = random.randint(1,len(score)-1)
                score[index] -= values[x][y]
                values[x][y] = 0
                print(f"bot{index} buzzed after {bot_buzz_time} seconds and",
                      " answered incorrectly correctly.\n The correct answer",
                       f" is: {correct_answers[x][y]}")
        else:
            # if player pressed first
            while True:
                answer = input("What is your answer: a,b,c, or d: ")
                if answer in abcd:
                    answer_index = abcd.index(answer)
                    break
                else:
                    print('invalid input')
            # check if right
            if answer_choices[answer_index] == correct_answers[x][y]:
                print("Correct!")
                score[0] += values[x][y]
                values[x][y] = 0
            else:
                print(f"incorrect. The correct answer is: {correct_answers[x][y]}")
                score[0] -= values[x][y]
                values[x][y] = 0
    else:

        # use the inputimeout for buzzer      
        try:
            buzz = inputimeout(prompt='buzz?', timeout=bot_buzz_time)

        except TimeoutOccurred:
            pass

        # if bots press first
        if buzz == None:
            if random.randint(1,100) <= num:
                # chose a random bot index and give them the score
                index = random.randint(1,len(score)-1)
                score[index] += values[x][y]
                values[x][y] = 0
                print(f"bot{index} buzzed after {bot_buzz_time} seconds and ",
                      f"answered correctly: {correct_answers[x][y]}")
            else:
                # chose a random bot index and subtract the score
                index = random.randint(1,len(score))
                score[index] -= values[x][y]
                values[x][y] = 0
                print(f"bot{index} buzzed after {bot_buzz_time} seconds and",
                      " answered incorrectly correctly.\n The correct answer",
                       f" is: {correct_answers[x][y]}")
        else:
            # if player pressed first, no multiple choice
            is_correct = False
            try:
                answer = inputimeout(prompt='what is your answer: ', timeout=10)
                is_correct = word_rounding(correct_answers[x][y].lower(), answer)
            except TimeoutOccurred:
                is_correct = False
            

            # check if right
            if is_correct:
                print("Correct!")
                score[0] += values[x][y]
                values[x][y] = 0
            else:
                print(f"incorrect. The correct answer is: {correct_answers[x][y]}")
                score[0] -= values[x][y]
                values[x][y] = 0


            



    
    




def main():
    # intro to game
    print("Hi, welcome to jeopardy!")
    print("Before we get started let's go over the format and rules:")
    print("1. There are 5 random catagories and 3 questions for each catagory")
    print("2. You will play with 1-3 bots")
    print("3. You have multiple choice on easy mode, not on hard mode")
    print("4. You have 10 sec to answer on hard mode, no time limit on easy")
    print("5. Everyone starts at 0 points")
    print("6. When choosing a question, you will be prompted for a catagory and value")
    print("7. You will compete to answer with buzzers. Enter any key to buzz")
    print("8. Answering correctly gains the points on the question, while answering incorrectly loses them")
    print("9. Unlike traditional jeopardy, there's no stealing")
    print("10. whoever has the most points by the end wins")
    start = input('enter any key to start the game')

    # settup
    num_bots, bot_difficulty, game_difficulty, board_width, catagories, questions, correct_answers, incorrect_answers  = settup_board()
   
    # set values and score
    values = [[100,200,300],[100,200,300],[100,200,300],[100,200,300],[100,200,300]]
    score = [0]
    for i in range(int(num_bots)):
        score.append(0)

    # game loop
    divisor = len(score)
    dividend = 0
    is_player = False
    for i in range(15):
        print_game_board(num_bots, catagories, board_width, values, score) 
        if dividend % divisor == 0:
            is_player = True
        else:
            is_player = False

        new_turn(num_bots, bot_difficulty, game_difficulty, 
                catagories, questions, correct_answers, 
                incorrect_answers, score, values, is_player)
        dividend += 1
    print_game_board(num_bots, catagories, board_width, values, score)
    
    # ending
    max_score = max(score)
    if score[0] == max_score:
        print(f"You Won with a Score of {max_score}!")
    else:
        print(f"You Lost to bot{score.index(max_score)} who had a Score of {max_score}.")
  
    

    


main()