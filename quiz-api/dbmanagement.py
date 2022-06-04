import sqlite3
import questions
import answers
import json
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
    cur.execute(querySql)
    cur.execute("commit")
    question.id = cur.lastrowid

def insertAnswers(answers: answers.Answer ):
    db_connection = sqlite3.connect("C:\\Users\\alexa\\Desktop\\web\\quiz-api\\db1.db")
    db_connection.isolation_level = None
    cur =db_connection.cursor()
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
    querySql = (f"DELETE FROM Questions WHERE position="+position)
    querySelect= f"""SELECT id FROM Questions WHERE position = {position}"""
    id= cur.execute(querySelect)
    idq = id.fetchone()[0]
    print(idq)
    cur.execute(querySql)
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
        WHERE position >= {questionUpdated.position}"""
        
    querySql=f"""UPDATE Questions
        SET text="{questionUpdated.text}",
        title="{questionUpdated.title}",
        position={questionUpdated.position},
        image="{questionUpdated.image}"
        WHERE position={position}"""
    querySelectAnswer=f""" SELECT id FROM Questions WHERE position = {position}"""
    id = cur.execute(querySelectAnswer)
    idq =id.fetchone()[0]
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
        cur.execute(querySql_all)
    

    # if int(position) == questionUpdated.position:
    #     print("dedans")
    #     querySelectAnswers= f""" SELECT id FROM Questions WHERE position = {position}"""
    #     id = cur.execute(querySelectAnswers)
    #     idQ = id.fetchone()[0]
    #     print(idQ)
    #     if( length < idQ):
    #         queryDelete = f"""DELETE FROM Answers WHERE id=(SELECT MAX(id) FROM Answers WHERE answers.questionId = questions.id)"""
    #         cur.execute(queryDelete)
            
    # else:
    #     cur_del=cur.execute(querySql_all)
    

    