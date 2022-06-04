# Exemple de création de classe en python
from cgitb import text

class Question():
    def __init__(self, title,position,text,image,possibleAnswers,id = None):
        self.title = title
        self.position = position
        self.text = text
        self.image = image
        self.possibleAnswers= possibleAnswers
        self.id = id