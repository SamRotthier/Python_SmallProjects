# This is a collection of a few small python projects.
I use this as a "Tryout Park" for Python.

## Learned lessons
- You can make a requirements file with the command "pip freeze > requirements.txt"
- When trying to use a overviewing file normal imports in the script won't always work, thats why you see some of these imports:
    try:
        from . import Responses  # Relative import for package execution
    except ImportError:
        import Responses   # Direct execution

# Course - 30 Great Python Projects
Most of the projects are from the Udemy course "30 Great Python Projects To Help You Master It In 2024"
## projects from the course:
1. Mad Libs 
2. Number Guessing 
3. Dice Simulator 
4. Hangman
5. Rock Paper Scissors
6. Password Generator
7. QR Code Generator
8. Website checker -> If the website is reachable
9. Common Password Checker
10. Brute Force -> Check brute forcing of a given password
11. Image Downloader
12. Tax Calculator -> with UI
13. File Sorter
14. Sentiment Analysis Bot -> For a text
15. URL Shortener
16. PDF Reader
17. Chat Bot
18. Email Scraper
19. Cryptocurrency Alerter -> alert for a certain value
20. Public Api
21. Habit Tracker -> tracks if you broke your habit yet
22. Currency Converter
23. Headline Scraper
24. Distance Calculator
25. Email Sender
26. Weather App
27. Value Prediction
28. Telegram Bot
29. Discord Bot
30. Dodgy Square

## Installed packages from course
Installed packages with "pip install" for this project:
- requests
- qrcode
- Pillow
- customtkinter
- fake_useragent
- textblob
- pypdf2
- selenium
- flask
- pandas
- tabulate
- beautifulsoup4
- geopy
- scikit-learn
- matplotlib
- python-telegram-bot
- discord
- pygame