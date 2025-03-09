from bots import *

bot1PayoffMatrix = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}
bot2PayoffMatrix = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}

def Game(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment):
    #bot1.rules(results, game_length, commitment, punishment, observation_cost, True)
    #bot2.rules(results, game_length, commitment, punishment, observation_cost, False)
    self.bot1 = bot1
    self.bot2 = bot2
    self.bot1PayoffMatrix = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}
    self.bot2PayoffMatrix = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}
    self.game_length = game_length
    self.commitment = commitment
    self.punishment = punishment

def rounds(self):
    for i in range(self.game_length):
        bot1Move = self.bot1.inTurn()
        bot2Move = self.bot2.inTurn()

        self.bot1.history.append(bot1Move) #adds self move in the odd indexes
        self.bot1.history.append(bot2Move)

        self.bot2.history.append(bot2Move)
        self.bot2.history.append(bot1Move)

        checkCommitmentAndPayoff(self.bot1)
        checkCommitmentAndPayoff(self.bot2)

    self.bot1.history = []
    self.bot2.history = []

def checkCommitmentAndPayoff(bot):
    pass

def gametime(self):
    pass


        