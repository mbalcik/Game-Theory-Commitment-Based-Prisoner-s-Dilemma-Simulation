import random
from datetime import datetime
class UnilateralOpenDeterministicGame():
    def __init__(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment):
        self.bot1 = bot1
        self.bot2 = bot2
        self.bot1PayoffMatrix = bot1PayoffMatrix
        self.bot2PayoffMatrix = bot2PayoffMatrix
        self.game_length = game_length
        self.commitment = commitment
        self.punishment = punishment
        self.gameHistory = []
    
    def takeUnilateralCommitment(self):
        self.bot1.makeCommitment = True
        self.bot2.makeCommitment = False
        bot1Commitment = self.bot1.makeUnilateralCommitment()

        if (bot1Commitment) :
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.commitment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.commitment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.punishment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.punishment})
        else : 
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.punishment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.punishment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.commitment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.commitment})

        return bot1Commitment
    
    def setOpponentCommitment(self):
        self.bot2.opponentCommitType = self.bot1.commitType


    def rounds(self):
        scores = [0, 0]
        for i in range(self.game_length):
            bot1Move = self.bot1.inTurn(i)
            bot2Move = self.bot2.inTurn(i)

            self.bot1.history.append(("C" if bot1Move else "D")) #adds self move in the even indexes starting w/ 0
            self.bot1.history.append(("C" if bot2Move else "D"))

            self.bot2.history.append(("C" if bot2Move else "D"))
            self.bot2.history.append(("C" if bot1Move else "D"))

            if (bot1Move) : self.bot1.coopCount += 1
            if (bot2Move) : self.bot2.coopCount += 1


            payoffs = self.checkCommitmentAndPayoff(i)
            scores[0] += payoffs[0]
            scores[1] += payoffs[1]

            roundStr = str(i)
            #print("This round moves: "+self.bot1.history[i]+self.bot1.history[i+1])
            #print("Round "+roundStr+" Bot 1 Budget: "+str(self.bot1.budget))
            #print("Round "+roundStr+" Bot 2 Budget: "+str(self.bot2.budget))
            
            
        #print(self.bot1.history)
        
        self.gameHistory = self.bot1.history
        self.bot1.history = []
        self.bot2.history = []

        self.bot1.makeCommitment = False
        self.bot2.makeCommitment = False

        historyString = ""
        for s in self.gameHistory:
            historyString += s

        return [historyString, scores]


    def checkCommitmentAndPayoff(self, roundNum):
        payoff1 = self.bot1PayoffMatrix.get(self.bot1.history[2*roundNum]+self.bot1.history[1+2*roundNum])
        payoff2 = self.bot2PayoffMatrix.get(self.bot2.history[2*roundNum]+self.bot2.history[1+2*roundNum])

        self.bot1.budget += payoff1
        self.bot2.budget += payoff2

        return [payoff1, payoff2]

    def gametime(self):
        commitment = self.takeUnilateralCommitment()
        self.setOpponentCommitment()
        historyAndPayoffs = self.rounds()

        return (historyAndPayoffs, commitment)

    def sendMatchupInfo(self):
        return [self.bot1.id, self.bot2.id, self.bot1.commitType, self.bot2.commitType, self.gameHistory]