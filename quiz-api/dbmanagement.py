import sqlite3
import questions
import answers
import json
import participants
#création d'un objet connection
# db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\E4FI\\E4FI-web\\quiz-app\\quiz-api\\db1.db")
# # set the sqlite connection in "manual transaction mode"
# # (by default, all execute calls are performed in their own transactions, not what we want)
# db_connection.isolation_level = None
# cur =db_connection.cursor()
# # start transaction
# cur.execute("begin")
# input_question="bonjour"
# # save the question to db
# insertion_result = cur.execute(
# 	f"insert into Question (title) values"
# 	f"('{input_question}')")

# #send the request
# cur.execute("commit")

#in case of exception, roolback the transaction
# cur.execute('rollback')
def insertQuestion(question: questions.Question):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur =db_connection.cursor()
    cur.execute("begin")
    querySql = (
            f"INSERT INTO Questions (position,title,text,image) VALUES"
            f"({question.position},'{question.title}','{question.text}','{question.image}')"
        )
    queryIsPositionTaken= f""" SELECT COUNT (*)  FROM Questions WHERE Questions.position = {question.position}"""
    
    isPositionTaken = cur.execute(queryIsPositionTaken).fetchone()[0]
    print("is position taken :")
    print(isPositionTaken)
    if(isPositionTaken>0):
        queryUpdate= f""" UPDATE Questions SET position = position +1 WHERE position >= {question.position}"""
        cur.execute(queryUpdate)
        cur.execute(querySql)
        cur.execute("commit")

    else:
        cur.execute(querySql)
        cur.execute("commit")

    question.id = cur.lastrowid

def insertAnswers(answers: answers.Answer ):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur =db_connection.cursor()
    answers.text = answers.text.replace("'", "''")
    cur.execute("begin")
    querySql = (
            f"INSERT INTO Answers (text,isCorrect,questionId) VALUES"
            f"('{answers.text}','{answers.isCorrect}',{answers.questionId})"
        )
    cur.execute(querySql)
    cur.execute("commit")
    

def deleteQuestion(position):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur =db_connection.cursor()
    cur.execute("begin")
    queryUpdate= f""" UPDATE Questions SET position = position -1 WHERE position >= {position}"""
    querySql = (f"DELETE FROM Questions WHERE position="+position)
    querySelect= f"""SELECT id FROM Questions WHERE position = {position}"""
    id= cur.execute(querySelect)
    idq = id.fetchone()[0]
    print(idq)
    cur.execute(querySql)
    cur.execute(queryUpdate)
    cur.execute("commit")
    return idq

def deleteAnswer(questionId):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur =db_connection.cursor()
    cur.execute("begin")
    querySql = (f"DELETE FROM Answers WHERE questionId="+ str(questionId))
    cur.execute(querySql)
    cur.execute("commit")

def getQuestion(position):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur =db_connection.cursor()

    querySql=(f"SELECT questions.text, title, position, image, answers.text, isCorrect FROM questions JOIN answers ON answers.questionId = questions.id WHERE questions.position = {position}")
    curexc=cur.execute(querySql)
    curRow = cur.fetchall()
    if(len(curRow)==0):
        return None
    answer = []
    for cur in curRow:
        if cur[5]=='False':
            isCorrect= False
        elif cur[5]=='True':
            isCorrect=True
        answer.append({
        'text' : cur[4],
        'isCorrect' : isCorrect
       })
    question = questions.Question(title=curRow[0][1], text=curRow[0][0], position=curRow[0][2], image=curRow[0][3],possibleAnswers= answer)
    db_connection.close()
    return question

def updateQuestion(position,questionUpdated: questions.Question,length):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur =db_connection.cursor()
    cur.execute("begin")
    querySql_all= f"""UPDATE Questions
        SET position=position+1
        WHERE position >= {questionUpdated.position} AND position < {position}"""
    
    querySql_allInverse= f"""UPDATE Questions
        SET position=position-1
        WHERE position <= {questionUpdated.position} AND position > {position}"""
        
    querySql=f"""UPDATE Questions
        SET text="{questionUpdated.text}",
        title="{questionUpdated.title}",
        position={questionUpdated.position},
        image="{questionUpdated.image}"
        WHERE position={position}"""
    
    querySelectAnswer=f""" SELECT id FROM Questions WHERE position = {position}"""
    id = cur.execute(querySelectAnswer)
    idq =id.fetchone()[0]
    queryUpdate= f""" UPDATE Questions SET position={questionUpdated.position} WHERE id={idq}"""
    queryCount = f"""SELECT COUNT(*) FROM Answers WHERE questionId={idq}"""
    count = cur.execute(queryCount)
    nbIdq = count.fetchone()[0]
    cur.execute("commit")
    if(int(position)== questionUpdated.position):
        print("position = question.position")
        cur.execute("begin")
        cur.execute(querySql)
        print(nbIdq)
        print(length)
        if length < nbIdq:
            print(" lenght > elaef")
            querySelectAnswer=f""" SELECT id FROM Questions WHERE position = {position}"""
            id = cur.execute(querySelectAnswer)
            idq =id.fetchone()[0]
            queryDelete = f""" DELETE FROM Answers WHERE questionId = {idq}"""
            cur.execute(queryDelete)
            cur.execute("commit")
            db_connection.close()
            for answ in questionUpdated.possibleAnswers:
                print(answ)
                answ= answers.Answer(answ["text"],answ["isCorrect"],idq)
                insertAnswers(answ)

    else:
        if(int(position) < questionUpdated.position):
            cur.execute(querySql_allInverse)
        else:
            cur.execute(querySql_all)
        cur.execute(queryUpdate)
    

def NumberOfQuestion():
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    try:

        question_data = """SELECT COUNT (*) FROM Questions"""
        count= cur.execute(question_data)
        count2= cur.fetchone()[0]
        return count2

    except Exception as e:
        print("exception")
        db_connection.close()
        raise RuntimeError(str(e))

def InsertParticipants(participant: participants.Participant):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    queryParticipant = f"""INSERT INTO Participants (playerName,score) VALUES ("{participant.playerName}",{participant.score})"""
    queryCount =f"""SELECT COUNT (*) FROM Participants WHERE playerName='{participant.playerName}'"""
    queryDeleteParticipant =f""" DELETE FROM Participants WHERE score <= {participant.score} AND playerName='{participant.playerName}'"""
    count = cur.execute(queryCount).fetchone()[0]
    print("la valeur de count :")
    print(count)
    # cur.execute(queryParticipant)
    if count >0:
        cur.execute(queryDeleteParticipant)
        cur.execute(queryParticipant)
    else:
        cur.execute(queryParticipant)
    cur.execute("commit")
    db_connection.close()
    return participant

    
def GetGoodAnswer():
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    queryGoodAnswer =f""" SELECT id FROM Answers WHERE isCorrect = 'True' """

    goodAnswer = cur.execute(queryGoodAnswer).fetchall()
    goodAnswerTab =[]
    for i in range(len(goodAnswer)):
        goodAnswerTab.append(int(goodAnswer[i][0]) - 4*i)
    print(goodAnswerTab)
    cur.execute("commit")
    db_connection.close()
    return goodAnswerTab

def DeleteAllParticipants():
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    queryDeleteParticipation = f"""DELETE FROM Participants"""
    cur.execute(queryDeleteParticipation)
    cur.execute("commit")
    db_connection.close()

def GetScore():
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    
    queryPlayerName=f"""SELECT DISTINCT playerName,score FROM Participants ORDER BY score DESC"""
    getPlayerName = cur.execute(queryPlayerName).fetchall()
    jsonScore=[]
    for data in getPlayerName:
        jsonScore.append({
            "playerName":data[0],
            "score": data[1]
        })
    cur.execute("commit")
    db_connection.close()
    return jsonScore

def numberOfParticipants():
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    try:

        number_participants = """SELECT COUNT (*) FROM Participants"""
        count= cur.execute(number_participants)
        count2= cur.fetchone()[0]
        return count2

    except Exception as e:
        print("exception")
        db_connection.close()
        raise RuntimeError(str(e))