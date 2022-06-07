import questions
import participants
def jsonToQuestion(payload):
    return questions.Question(payload["title"],payload["position"],payload["text"],payload["image"],payload['possibleAnswers'])

def questionToJson(question: questions.Question):
    return {"title":question.title,"position":question.position,"text":question.text,"image":question.image,"possibleAnswers":question.possibleAnswers }

def jsonToParticipant(payload):
    return participants.Participant(payload["playerName"],payload["answers"],0)

def participantToJson(participant: participants.Participant):
    return {"playerName": participant.playerName, "answers":participant.answers, "score": participant.score}