from flask import Flask, request
from flask_cors import CORS
import jwt_utils
import functions

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return functions.hello_world()

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return functions.GetQuizInfo()

@app.route('/login',methods=['POST'])
def login():
	return functions.login()

@app.route('/questions',methods=['POST'])
def PostQuestion():
	return functions.PostQuestion()

@app.route('/questions/<position>',methods=['DELETE'])
def DelQuestion(position):
	return functions.DelQuestion(position)

@app.route('/questions/<position>',methods=['GET'])
def GetQuestion(position):
	return functions.GetQuestion(position)

@app.route('/questions/<position>',methods=['PUT'])
def UpdateQuestion(position):
	return functions.UpdateQuestion(position)

@app.route('/getNumberOfQuestion',methods=['GET'])
def GetNumberOfQuestion():
	return functions.GetNumberOfQuestion()

@app.route('/participations',methods=['POST'])
def PostParticipants():
	return functions.PostParticipants()

@app.route('/participations', methods=['DELETE'])
def DeleteParticipants():
	return functions.DelAllParticipants()

if __name__ == "__main__":
    app.run()