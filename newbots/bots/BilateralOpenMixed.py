import random
from datetime import datetime

class BilateralOpenMixed():
    bot_number = 0
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.seed = seed
        BilateralOpenMixed.bot_number += 1
        self.id = BilateralOpenMixed.bot_number
        self.coopCount = 0

    def getID(self):
        return self.id
    
    def getBudget(self):
        return self.budget

    def makeMixedCommitment(self):
        self.seed = datetime.now().timestamp()
        return self.coopCommitProb, self.seed

    def setOpponentCoopCommit(self, opponentCommitProb):
        self.opponentCommitProb = opponentCommitProb

    def inTurn(self, roundNum):
        return self.mostCoopStrat.play(self.history, self.budget, roundNum)
    