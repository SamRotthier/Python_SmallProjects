# pip install textblob
#examples:
# I am super happy today!
# Today sucks!

from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_treshold: float = sensitivity
    hostile_treshold: float = sensitivity

    if polarity >= (friendly_treshold):
        return Mood('😊', polarity)
    elif polarity <= hostile_treshold:
        return Mood('Angry', polarity)
    else:
        return Mood('😐', polarity)

def run_sentiment_bot():
    print('Enter some text to get a sentiment analysis back:')
    while True:
        user_input: str = input('You: ')
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')

if __name__ == '__main__':
    run_sentiment_bot()