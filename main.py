
from Games.MathLibs import *
from Games.RandomNumber import * 
from Games.DiceSimulator import *
from Games.Hangman import * 
from Games.RockPaperScissors import *

while True:
    try:
        print("What would you like to do:")
        print("1)Games")
        print("2)DataScience")
        subject_Choice : int = int(input('Choice: '))
    except ValueError as e:
        print('Please eneter a valid number.')
        continue


    if (subject_Choice == 1):
        try:
            print("What would game would you like to play:")
            print("1)Math Libs")
            print("2)Random Number (1-10)")
            print("3)Dice Simulator")
            print("4)Hangman")
            print("5)Rock paper scissors")
            game_Choice : int = int(input('Choice: '))
        except ValueError as e:
            print('Please eneter a valid number.')
            continue

        if (game_Choice == 1):
            mathLibs_Game()
            continue
        elif(game_Choice == 2):
            random_number()
            continue
        elif(game_Choice == 3):
            DiceSimulator_main()
            continue
        elif(game_Choice == 4):
            Hangman_game()
            continue
        elif(game_Choice == 5):
            RPS_Game()
            continue




