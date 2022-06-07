from cgitb import text

class Participant():
    def __init__(self, playerName,answers,score,id = None):
        self.playerName = playerName
        self.answers = answers
        self.score= score
        self.id = id