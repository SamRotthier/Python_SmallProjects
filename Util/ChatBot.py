from difflib import get_close_matches

brain: dict= {'hello': 'Hey there!',
                      'how are you': 'I am good, thanks!',
                      'what time is it': 'Don\'t know, dont\'t care...',
                      'bye' : 'See you!'}

def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    # Return the first best match, else return None
    if matches: 
        return matches[0]
    
def chat_bot(knowledge: dict):
    """Chatbot"""
    while True:
        user_input: str = input('You: ')

        # Finds the best match, otherwise returns None
        best_match: str | None = get_best_match(user_input, knowledge)

        # Gets the best match from the knowledge base
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand...')

def chat_bot_start():
    chat_bot(knowledge=brain)

if __name__ == '__main__':
    chat_bot(knowledge=brain)

# Improvements:
#   - Make/load a JSON file instead of the brain in the code
#   - Extra functionality like ask for the time