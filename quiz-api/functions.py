from numbers import Number
from flask import Flask, request
from answers import Answer
import jwt_utils
from mapping import jsonToParticipant, participantToJson, questionToJson,jsonToQuestion
import dbmanagement
from participants import Participant

def hello_world():
	x = 'world'
	return f"Hello, {x}"

def GetQuizInfo():
    score = dbmanagement.GetScore()
    n = dbmanagement.NumberOfQuestion()
    return {"size": n,"scores": score},200

def login():
	password = "Vive l'ESIEE !"
	payload = request.get_json()
	if(password == payload["password"]):
		token= jwt_utils.build_token()
		return {"token": token},200
	else:
		return {"error":401,"message":" Wrong password","payload":payload["password"],"password":password},401

def PostQuestion():
    try:
        if request.headers.get('Authorization'):
            payload = request.get_json()
            for id, element in enumerate(payload):
                if isinstance(payload[element], str):
                    payload[element] = payload[element].replace("'", "''")
            question = jsonToQuestion(payload)
            dbmanagement.insertQuestion(question)
            answers = payload['possibleAnswers']
            for answ in answers:
                answ= Answer(answ["text"],answ["isCorrect"],question.id)
                dbmanagement.insertAnswers(answ)
            return {"message": "la question a bien été insert"},200
        else:
            print("else")
            return {"message": "la question n'a pas été insert","error":"401"},401
    except Exception as e:
        print("exception")
        return {"message":"le try a échoué","error":"401"},401

def DelQuestion(position):
    try:
        if request.headers.get('Authorization'):
            question = dbmanagement.getQuestion(position)
            if(question is None):
                return {"message":" la question n'existe pas "},404
            id = dbmanagement.deleteQuestion(position)
            dbmanagement.deleteAnswer(id)
            return {"message":"la question a été supprimé"},204
        else:
            return{"message":"la suppression de la question a échoué","error":"401"},401
    except:
        return{"message":"le try a échoué","error":"401"},401

def GetQuestion(position):
    try:
        question = dbmanagement.getQuestion(position)
        if(question is None):
            return {"message":f"Question with position {position} not found","error":"404"},404
        return questionToJson(question),200
    except:
        return{"message":"try a échoué"},401

def UpdateQuestion(position):
    try:
        if request.headers.get('Authorization'):
            question = dbmanagement.getQuestion(position)
            if(question is None):
                return {"message":" la question n'existe pas"},404
            payload=request.get_json()
            question = jsonToQuestion(payload)
            dbmanagement.updateQuestion(position,question,len(payload['possibleAnswers']))
            return questionToJson(question)
        else:
            return {"message":f"pas réussi à update la question avec la position {position}","error":"404"},404

    except:
        return{"message":"try a échoué"},401

def GetNumberOfQuestion():
    try:
        return str(dbmanagement.NumberOfQuestion()),200
    except:
        return {"message":"try a échoué"},401

def PostParticipants():
    # try:
    payload= request.get_json()
    tabGoodAnswer=dbmanagement.GetGoodAnswer()
    participant = jsonToParticipant(payload)
    if len(participant.answers) != int(GetNumberOfQuestion()[0]):
        print("number of participant answers :" + str(len(participant.answers)))
        print("number of question : "+ str(GetNumberOfQuestion()[0]))
        return {"message":"wrong number of answers","error":"400"},400
    # participant.score = 0
    print(" __________________________")
    print( tabGoodAnswer)
    for i in range (len(tabGoodAnswer)):
        if tabGoodAnswer[i] == participant.answers[i]:
            participant.score += 1
    print(" __________________________")
    print(participant.score)
    participants = dbmanagement.InsertParticipants(participant)
    return participantToJson(participants),200

    # except:
    #     return{"message": "try a échoué", "error": "401"},401

def DelAllParticipants ():
    try:
        n = dbmanagement.numberOfParticipants()
        if n==0:
            return{"message":"il n'y a pas de participants"},204
        else:
            dbmanagement.DeleteAllParticipants()
            return {"message": " participants ont été supprimé"},204
    except:
        return{"message": "try a échoué", "error": "401"},401



