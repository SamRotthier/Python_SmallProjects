from difflib import get_close_matches

brain: dict= {'hello': 'Hey there!',
                      'how are you': 'I am good, thanks!',
                      'what time is it': 'Don\'t know, dont\'t care...',
                      'bye' : 'See you!'}

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches: 
        return matches[0]
    
def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand...')

def chat_bot_start():
    chat_bot(knowledge=brain)

if __name__ == '__main__':
    chat_bot(knowledge=brain)