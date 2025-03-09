import random
from datetime import datetime


class BilateralClosedDeterministic():
    bot_number = 0

    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType):
        #super().__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType)
        
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.assumeCommitProb = assumeCommitProb
        self.commitType = commitType #true for coop, false for defect
        self.opponentCoopCommitType = opponentCoopCommitType
        BilateralClosedDeterministic.bot_number += 1
        self.id = BilateralClosedDeterministic.bot_number
        self.coopCount = 0
    
    def getID(self):
        return self.id
    
    def getBudget(self):
        return self.budget

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def assumeOpponentCommit(self):
        random.seed(datetime.now().timestamp())
        if (random.randrange(1,101) < self.assumeCommitProb) : self.opponentCoopCommitType = True
        else : self.opponentCoopCommitType = False

    def makeCommitment(self):
        random.seed(datetime.now().timestamp())
        if (random.randrange(1,101) < self.coopCommitProb) : 
            self.setCommitType(True)
            return self.commitType #return cooperation commitment if true
        else : 
            self.setCommitType(False)
            return self.commitType #return defection commitment if false

    def inTurn(self, roundNum):
        #print(self.history)
        if (self.commitType & self.opponentCoopCommitType) : return self.mostCoopStrat.play(self.history, self.budget, roundNum) # both coop commit
        elif (self.commitType &  (not self.opponentCoopCommitType)) : return self.lessCoopStrat.play(self.history, self.budget, roundNum) # self coop commit
        elif ((not self.commitType)  & self.opponentCoopCommitType) : return self.lessDefectStrat.play(self.history, self.budget, roundNum) # self defect commit
        else : return self.mostDefectStrat.play(self.history, self.budget, roundNum) # both defect commit

    
        
    def stratName(self):
        if (self.commitType & self.opponentCoopCommitType) : return self.mostCoopStrat.name() # both coop commit
        elif (self.commitType &  (not self.opponentCoopCommitType)) : return self.lessCoopStrat.name() # self coop commit
        elif ((not self.commitType)  & self.opponentCoopCommitType) : return self.lessDefectStrat.name() # self defect commit
        else : return self.mostDefectStrat.name() # both defect commit

        