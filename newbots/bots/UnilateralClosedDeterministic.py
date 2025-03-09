import random
from datetime import datetime


class UnilateralClosedDeterministic():
    bot_number = 0
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.assumeCommit = assumeCommitProb
        self.makeCommitment = False
        self.commitType = commitType #true for coop, false for defect
        self.opponentCoopCommitType = opponentCoopCommitType
        UnilateralClosedDeterministic.bot_number += 1
        self.id = UnilateralClosedDeterministic.bot_number
        self.coopCount = 0
    
    def getID(self):
        return self.id
    
    def getBudget(self):
        return self.budget

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def makeUnilateralCommitment(self):
            random.seed(datetime.now().timestamp())
            if (random.randrange(1,101) < self.coopCommitProb) : 
                self.setCommitType(True)
                return self.commitType #return cooperation commitment if true
            else : 
                self.setCommitType(False)
                return self.commitType #return defection commitment if false



    def assumeOpponentCommit(self):
        if (random.randrange(1,101) < self.assumeCommit) : self.opponentCoopCommitType = True
        else : self.opponentCoopCommitType = False

    def inTurn(self, roundNum):
        if (self.makeCommitment) :
            if (self.commitType) : return self.mostCoopStrat.play(self.history, self.budget, roundNum) # both coop commit
            else : return self.mostDefectStrat.play(self.history, self.budget, roundNum) # both defect commit
        else : 
            if (self.opponentCoopCommitType) : return self.mostCoopStrat.play(self.history, self.budget, roundNum) # both coop commit
            else : return self.mostDefectStrat.play(self.history, self.budget, roundNum) # both defect commit


