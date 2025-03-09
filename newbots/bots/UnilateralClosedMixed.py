import random
from datetime import datetime

class UnilateralClosedMixed():
    bot_number = 0
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeOpponentCommitProb, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.assumeCommitProb = assumeOpponentCommitProb
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.makeCommitment = False
        self.seed = seed
        UnilateralClosedMixed.bot_number += 1
        self.id = UnilateralClosedMixed.bot_number
        self.coopCount = 0

    def getID(self):
        return self.id
    
    def getBudget(self):
        return self.budget

    def makeUnilateralCommitment(self):
        self.seed = datetime.now().timestamp()
        return self.coopCommitProb, self.seed

    def assumeOpponentCommit(self):
        self.opponentCoopCommitProb = self.assumeCommitProb

    def inTurn(self, roundNum):
        return self.mostCoopStrat.play(self.history, self.budget, roundNum)
