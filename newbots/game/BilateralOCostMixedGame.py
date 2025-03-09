import random
from datetime import datetime


class BilateralOCostMixedGame():
    def __init__(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment, observation_cost):
        self.bot1 = bot1
        self.bot2 = bot2
        self.bot1PayoffMatrix = bot1PayoffMatrix
        self.bot2PayoffMatrix = bot2PayoffMatrix
        self.game_length = game_length
        self.commitment = commitment
        self.punishment = punishment
        self.observation_cost = observation_cost
        self.bot1CommitMoves = []
        self.bot2CommitMoves = []
        self.gameHistory = []        
    
    def takeBilateralCommitment(self):
            bot1CommitProb, bot1Seed = self.bot1.makeMixedCommitment()
            random.seed(bot1Seed)
            for i in range(self.game_length):
                if (random.randrange(1,101) <= bot1CommitProb) : 
                        self.bot1CommitMoves.append("C")
                else : 
                    self.bot1CommitMoves.append("D")
            bot2CommitProb, bot2Seed = self.bot2.makeMixedCommitment()
            random.seed(bot1Seed)
            for i in range(self.game_length):
                if (random.randrange(1,101) <= bot2CommitProb) : 
                    self.bot2CommitMoves.append("C")
                else : 
                    self.bot2CommitMoves.append("D")

            return [bot1CommitProb, bot2CommitProb]

        
    def payForCommitment(self):
        bot1pays = self.bot1.payObservationCost()
        bot2pays = self.bot2.payObservationCost()
        
        
        if (bot1pays) :
            self.bot1.budget -= self.observation_cost
            self.bot1.setOpponentCoopCommit(self.bot2.coopCommitProb)
        else : 
            self.bot1.assumeOpponentCommit()

        if (bot2pays) :
            self.bot2.budget -= self.observation_cost
            self.bot2.setOpponentCoopCommit(self.bot1.coopCommitProb)
        else : 
            self.bot2.assumeOpponentCommit()

        return [bot1pays, bot2pays]


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

        self.gameHistory = self.bot1.history
        self.bot1.history = []
        self.bot2.history = []

        self.bot1.opponentCoopCommitProb = 0
        self.bot2.opponentCoopCommitProb = 0
        
        historyString = ""
        for s in self.gameHistory:
            historyString += s

        return [historyString, scores]


    def checkCommitmentAndPayoff(self, roundNum):
        payoff1 = self.bot1PayoffMatrix.get(self.bot1.history[2*roundNum]+self.bot1.history[1+2*roundNum])
        payoff2 = self.bot2PayoffMatrix.get(self.bot2.history[2*roundNum]+self.bot2.history[1+2*roundNum])
        if (self.bot1CommitMoves[roundNum] == self.bot1.history[2*roundNum]) :
            payoff1 += self.commitment
        else : 
            payoff1 += self.punishment
    
        if (self.bot2CommitMoves[roundNum] == self.bot2.history[2*roundNum]) :
            payoff2 += self.commitment
        else : 
            payoff2 += self.punishment
        
        self.bot1.budget += payoff1
        self.bot2.budget += payoff2

        return [payoff1, payoff2]




    def gametime(self):
        commitments = self.takeBilateralCommitment()
        observeds = self.payForCommitment()
        historyAndPayoffs = self.rounds()
        seedlists = [self.seedListToStr(self.bot1CommitMoves), self.seedListToStr(self.bot2CommitMoves)]


        return (historyAndPayoffs, commitments, observeds, seedlists)

    def sendMixedMatchupInfo(self):
        return [self.bot1.id, self.bot2.id, self.bot1CommitMoves, self.bot2CommitMoves, self.gameHistory]
    
    def seedListToStr(self, seedList): 
        str = ""
        for s in seedList:
            str += s
        return str