from Games.MathLibs import *
from Games.RandomNumber import * 
from Games.DiceSimulator import *
from Games.Hangman import * 
from Games.RockPaperScissors import *
from Util.PasswordGenerator import *
from Util.QRCodeGenerator.QRCodeGenerator import *
from Util.WebsiteChecker.WebsiteChecker import *
from Util.PasswordChecker.PasswordChecker import *
from Util.BruteForce.BruteForce import *
from Util.ImageDownloader.ImageDownloader import *
from Util.TaxCalculator import *
from Util.FileSorter import *
from Util.SentimentAnalysisBot import *
from Util.UrlShortener import *
from Util.PdfTextExtractor.PdfReader import *
from Util.ChatBot import *


while True:
    try:
        print("What would you like to do:")
        print("1)Games")
        print("2)Utils")
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

    if (subject_Choice == 2):
        try:
            print("What Util would u like to use:")
            print("1)Password Generator")
            print("2)QR Code Generator")
            print("3)Website Checker")
            print("4)Password Checker")
            print("5)Brute Force tester")
            print("6)Image Downloader")
            print("7)Tax calculator (front end)")
            print("8)File Sorter")
            print("9)Sentiment Analysis Bot")
            print("10)URL Shortener")
            print("11)PDF Reader")
            print("12)Chat Bot")
            Util_Choice : int = int(input('Choice: '))
        except ValueError as e:
            print('Please eneter a valid number.')
            continue

        if (Util_Choice == 1):
            password_generator_start()
            continue
        elif(Util_Choice == 2):
            main_QRCodeGen()
            continue
        elif(Util_Choice == 3):
            main_websiteChecker()
            continue
        elif(Util_Choice == 4):
            main_passwordChecker()
            continue
        elif(Util_Choice == 5):
            main_bruteForce()
            continue
        elif(Util_Choice == 6):
            main_imageDownloader()
            continue
        elif(Util_Choice == 7):
            main_taxCalc()
            continue
        elif(Util_Choice == 8):
            main_file_sorter()
            continue
        elif(Util_Choice == 9):
            run_sentiment_bot()
            continue
        elif(Util_Choice == 10):
            main_url_shortener()
            continue
        elif(Util_Choice == 11):
            main_pdf_reader()
            continue
        elif(Util_Choice == 12):
            chat_bot_start()
            continue



