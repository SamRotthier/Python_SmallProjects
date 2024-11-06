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
    """
    Analyze the mood of a given text and return a Mood object containing the emoji and sentiment polarity.

    :param input_text: The input text to be analyzed
    :param sensitivity: 0.0 (super sensitive) - 1.0 (ultra nonsensitive)
    :return: A Mood object containing the emoji representing the mood and the sentiment polarity value
    """
    polarity: float = TextBlob(input_text).sentiment.polarity

    # Define mood thresholds
    friendly_treshold: float = sensitivity
    hostile_treshold: float = sensitivity

    # Determine the mood and return the corresponding emoji
    if polarity >= (friendly_treshold):
        return Mood('😊', polarity)
    elif polarity <= hostile_treshold:
        return Mood('Angry', polarity)
    else:
        return Mood('😐', polarity)

def run_sentiment_bot():
    print('Enter some text to get a sentiment analysis back:')
    while True:
        user_input: str = input('You: ') # Try it with emojis as well! :) :O :D :( :I
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')

if __name__ == '__main__':
    run_sentiment_bot()