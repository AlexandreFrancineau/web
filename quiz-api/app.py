from flask import Flask, request
import jwt_utils
import functions

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(ssl_context='adhoc')