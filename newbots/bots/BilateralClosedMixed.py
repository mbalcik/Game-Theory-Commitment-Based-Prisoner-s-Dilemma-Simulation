import random
from datetime import datetime

#seed will be determined everytime bot makes a commitment, dummy value entered in construction
#opponentCommitProb is equal to assumeCommitProb, dummy value entered in construction

class BilateralClosedMixed():
    bot_number = 0

    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, opponentCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.assumeCommitProb = assumeCommitProb
        self.opponentCommitProb = opponentCommitProb
        self.seed = seed
        BilateralClosedMixed.bot_number += 1
        self.id = BilateralClosedMixed.bot_number
        self.coopCount = 0
    
    def getID(self):
        return self.id
    
    def getBudget(self):
        return self.budget

    def makeMixedCommitment(self):
        self.seed = datetime.now().timestamp()
        return self.coopCommitProb, self.seed


    def assumeOpponentCommit(self):
        self.opponentCommitProb = self.assumeOpponentCommit

    def inTurn(self, roundNum):
        #print(self.history)
        return self.mostCoopStrat.play(self.history, self.budget, roundNum)
    