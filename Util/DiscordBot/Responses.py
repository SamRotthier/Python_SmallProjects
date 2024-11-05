from difflib import get_close_matches
import json
import os

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0] #should give back the best matching match
    
def get_response(message: str, knowlegde: dict) -> str:
    best_match: str | None = get_best_match(message, knowlegde)

    if answer:= knowlegde.get(best_match):
        return answer
    else:
        return 'I don\'t understand... Could you try rephrasing that?'
    
def load_knowledge(file: str) -> dict:
    with open(file, 'r') as f:
        return json.load(f)
    
if __name__ == '__main__':
    KnowledgeJson: str = os.path.join(os.path.dirname(__file__), 'Knowledge.json')
    test_knowledge: dict= load_knowledge(KnowledgeJson)    
    test_response: str= get_response('hello', knowlegde=test_knowledge)
    print(test_response)