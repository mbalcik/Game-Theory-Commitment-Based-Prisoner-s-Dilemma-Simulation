import random
from datetime import datetime


class UnilateralOCostDeterministic():
    bot_number = 0
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.assumeCommitProb = assumeCommitProb
        self.payProb = payProb
        self.makeCommitment = False
        self.commitType = commitType #true for coop, false for defect
        self.opponentCoopCommitType = opponentCoopCommitType
        UnilateralOCostDeterministic.bot_number += 1
        self.id = UnilateralOCostDeterministic.bot_number
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

    


    def payObservationCost(self):
        if (random.randrange(1,101) <= self.payProb) : return True
        else : return False


    def assumeOpponentCommit(self):
        if (random.randrange(1,101) < self.assumeCommitProb) : self.opponentCoopCommitType = True
        else : self.opponentCoopCommitType = False
    
    def setOpponentCoopCommit(self, opponentCoopCommitType):
        self.opponentCoopCommitType = opponentCoopCommitType

    def inTurn(self, roundNum):
        if (self.makeCommitment) :
            if (self.commitType) : return self.mostCoopStrat.play(self.history, self.budget, roundNum) # both coop commit
            else : return self.mostDefectStrat.play(self.history, self.budget, roundNum) # both defect commit
        else : 
            if (self.opponentCoopCommitType) : return self.mostCoopStrat.play(self.history, self.budget, roundNum) # both coop commit
            else : return self.mostDefectStrat.play(self.history, self.budget, roundNum) # both defect commit


