import random
from datetime import datetime

class BilateralOCostMixed():
    bot_number = 0
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, payProb, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.assumeCommit = assumeCommitProb
        self.payProb = payProb
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.seed = seed
        BilateralOCostMixed.bot_number += 1
        self.id = BilateralOCostMixed.bot_number
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

    def payObservationCost(self):
        random.seed(datetime.now().timestamp())
        if (random.randrange(1,101) <= self.payProb) : return True
        else : return False

    def assumeOpponentCommit(self):
        self.opponentCoopCommitProb = self.assumeCommit

    def inTurn(self, roundNum):
        return self.mostCoopStrat.play(self.history, self.budget, roundNum)
    