from Games.DiceSimulator import DiceSimulator_main
from Games.DodgySquare import main_run_DS
from Games.Hangman import Hangman_game
from Games.MathLibs import mathLibs_Game
from Games.RandomNumber import random_number
from Games.RockPaperScissors import RPS_Game
from Util.BruteForce.BruteForce import main_bruteForce
from Util.ChatBot import chat_bot_start
from Util.CryptoAlerter.CryptoAlerter import main_run_cryptoAlerter
from Util.CurrencyConverter.CurrencyConverter import main_currencyConverter
from Util.DiscordBot.DiscordBot import run_bot
from Util.DistanceConverter import main_distanceConverter
from Util.EmailScraper.EmailScraper import main_email_scraper
from Util.EmailSender.SendEmail import send_email
from Util.FileSorter import main_file_sorter
from Util.HabitTracker.HabitMain import main_habitTracker
from Util.HeadlineScraper import main_headlineScraper
from Util.ImageDownloader.ImageDownloader import main_imageDownloader
from Util.PasswordChecker.PasswordChecker import main_passwordChecker
from Util.PasswordGenerator import password_generator_start
from Util.PdfTextExtractor.PdfReader import main_pdf_reader
from Util.PublicApi import main_run_publicApi
from Util.QRCodeGenerator.QRCodeGenerator import main_QRCodeGen
from Util.SentimentAnalysisBot import run_sentiment_bot
from Util.TaxCalculator import main_taxCalc
from Util.TelegramBot import main_telegramBot
from Util.UrlShortener import main_url_shortener
from Util.ValuePredition.ValuePrediction import run_valuePrediction
from Util.WebsiteChecker.WebsiteChecker import main_websiteChecker
from Util.WheaterApp.WheaterApp import main_weatherApp



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
            print("6)Dodgy Square")
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
        elif(game_Choice == 6):
            main_run_DS()
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
            print("13)Email Scraper")
            print("14)Cryptocurrency Alerter")
            print("15)Public Api")
            print("16)Habit Tracker")
            print("17)Currency Converter")
            print("18)Headline Scraper")
            print("19)Distance Calculator")
            print("20)Email Sender")
            print("21)Weather App")
            print("22)Value Prediction (linear)")
            print("23)Telegram Bot")
            print("24)Discord Bot")
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
        elif(Util_Choice == 13):
            print('Emails will get scraped from:')
            print('https://www.randomlists.com/email-addresses?qty=50')
            # Improvement idea: Make it so user can input his's own value
            main_email_scraper()
            continue
        elif(Util_Choice == 14):
            print('Will alert for:')
            print('btc, bottom=20_000, top=28_000')
            print('eth, bottom=1800, top=1900')
            print('xrp, bottom=0.47, top=0.48')
            # Improvement idea: Make it so user can input his's own crypto's to a list that will be tracked
            main_run_cryptoAlerter()
            continue
        elif(Util_Choice == 15):
            main_run_publicApi()
            continue
        elif(Util_Choice == 16):
            print('Will track for:')
            print('Coffee, datetime(2023,5,6,8), cost=1, minutes_used=5')
            print('Wasting time, datetime(2024,10,29,6), cost=100, minutes_used=60 * 12')
            # Improvement idea: Make it so user can input his's habits to track
            main_habitTracker()
            continue
        elif(Util_Choice == 17):
            print('Will convert for:')
            print('100,EUR,JPY, rates=rates)')
            # Improvement idea: Make it so user can input his's habits to track
            main_currencyConverter()
            continue
        elif(Util_Choice == 18):
            print('Will scrape headline from:')
            print('https://www.bbc.com/news')
            # Improvement idea: Make it so user can input his's own website to scrape
            main_headlineScraper()
            continue
        elif(Util_Choice == 19):
            main_distanceConverter()
            continue
        elif(Util_Choice == 20):
            #No email coupled so won't work currently
            send_email(to_email='test_email@fastmail.com', 
                   subject='Hey there buddy', 
                   body='Hello there! I send you an image of my cat!',
                   image='cat.png')
            continue
        elif(Util_Choice == 21):
            main_weatherApp()
            continue
        elif(Util_Choice == 22):
            print('Will give a prediction for:')
            print('years: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
            print('earnings: list[int] = [1000, 800 ,2000, 1500, 3400, 3700, 4000, 3800, 5000, 4800]')
            print('my_input: int = 20')
            # Improvement idea: Make it so user can input his's own data
            run_valuePrediction()
            continue
        elif(Util_Choice == 23):
            #No Telegram bot coupled so won't work currently
            main_telegramBot()
            continue
        elif(Util_Choice == 24):
            #No Discord bot coupled so won't work currently
            run_bot()
            continue
