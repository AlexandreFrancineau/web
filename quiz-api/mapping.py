import questions
def jsonToQuestion(payload):
    return questions.Question(payload["title"],payload["position"],payload["text"],payload["image"],payload['possibleAnswers'])

def questionToJson(question: questions.Question):
    return {"title":question.title,"position":question.position,"text":question.text,"image":question.image,"possibleAnswers":question.possibleAnswers }