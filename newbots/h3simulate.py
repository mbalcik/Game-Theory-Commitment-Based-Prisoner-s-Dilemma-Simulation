from tournament import tournament
import math
from bots.BilateralClosedDeterministic import BilateralClosedDeterministic
from game.BilateralClosedDeterministicGame import BilateralClosedDeterministicGame
from bots.BilateralClosedMixed import BilateralClosedMixed
from game.BilateralClosedMixedGame import BilateralClosedMixedGame
from bots.BilateralOCostDeterministic import BilateralOCostDeterministic
from game.BilateralOCostDeterministicGame import BilateralOCostDeterministicGame
from bots.BilateralOCostMixed import BilateralOCostMixed
from game.BilateralOCostMixedGame import BilateralOCostMixedGame
from bots.BilateralOpenMixed import BilateralOpenMixed
from game.BilateralOpenMixedGame import BilateralOpenMixedGame
from bots.BilateralOpenDeterministic import BilateralOpenDeterministic
from game.BilateralOpenDeterministicGame import BilateralOpenDeterministicGame
from bots.UnilateralClosedDeterministic import UnilateralClosedDeterministic
from game.UnilateralClosedDeterministicGame import UnilateralClosedDeterministicGame
from bots.UnilateralClosedMixed import UnilateralClosedMixed
from game.UnilateralClosedMixedGame import UnilateralClosedMixedGame
from bots.UnilateralOCostDeterministic import UnilateralOCostDeterministic
from game.UnilateralOCostDeterministicGame import UnilateralOCostDeterministicGame
from bots.UnilateralOCostMixed import UnilateralOCostMixed
from game.UnilateralOCostMixedGame import UnilateralOCostMixedGame
from bots.UnilateralOpenDeterministic import UnilateralOpenDeterministic
from game.UnilateralOpenDeterministicGame import UnilateralOpenDeterministicGame
from bots.UnilateralOpenMixed import UnilateralOpenMixed
from game.UnilateralOpenMixedGame import UnilateralOpenMixedGame

from strategies.TitForTat import TitForTat
from strategies.TitForTwoTats import TitForTwoTats
from strategies.Pavlov import Pavlov
from strategies.GrimTrigger import GrimTrigger
from strategies.AlwaysDefect import AlwaysDefect
from strategies.AlwaysCooperate import AlwaysCooperate
from strategies.GenerousTitForTat import GenerousTitForTat
from strategies.Randomized import Randomized



titForTat = TitForTat()
titForTwoTats = TitForTwoTats() 
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect() 
alwaysCooperate = AlwaysCooperate()
generousTitForTat = GenerousTitForTat()
randomized = Randomized(50)

"BilateralDeterministic: 0,4"
"BilateralMixed: 1,5"
"UnilateralDeterministic 6,10"
"UnilalteralMixed 7,11"

#Bilateral Closed Deterministic = 0, Bilateral Open Deterministic = 4
#strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCommitType
playerTypes0 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 100, False, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 100, False, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 100, False, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 100, False, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 100, False, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 100, False, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 100, False, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 100, False, False]]
playerWeights0 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#BilateralOpenDeterministic, strategies, budget, coopCommitProb, commitType, opponentCoopCommitType
playerTypes4 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, False, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, False, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, False, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, False, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, False, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, False, False]]
playerWeights4 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]



#Bilateral Closed Mixed = 1, Bilateral Open Mixed = 5
                #BilateralClosedMixed strategies, budget, coopCommitProb, assumeCommitProb, opponentCommitProb, seed
playerTypes1 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 50, 100, 0, 2],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 50, 100, 0, 1],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 50, 100, 0, 3],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 50, 100, 0, 4],
               [titForTat, pavlov, grimTrigger, randomized, 0, 50, 100, 0, 1],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 50, 100, 0, 3],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 100, 0, 1],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 50, 100, 0, 3]]
playerWeights1 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

                #BilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
playerTypes5 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 50, 0, 2],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 50, 0, 1],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 50, 0, 3],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 50, 0, 4],
               [titForTat, pavlov, grimTrigger, randomized, 0, 50, 0, 1],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 50, 0, 3],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 0, 1],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 50, 0, 3]]
playerWeights5 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]



#UnilateralClosedDeterministic, strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType
playerTypes6 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 100, False, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 100, False, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 100, False, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 100, False, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 100, False, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 100, False, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 100, False, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 100, False, False]]
playerWeights6 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#UnilateralOpenDeterministic, budget, coopCommitProb, commitType, opponentCoopCommitType
playerTypes10 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, False, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, False, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, False, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, False, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, False, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, False, False]]
playerWeights10 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]




#Unilateral Closed Mixed = 7, Unilateral Open Mixed = 11
                #UnilateralClosedMixed, strategies, budget, coopCommitProb, assumeOpponentCommitProb, opponentCoopCommitProb, seed
playerTypes7 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 50, 100, 100, 0],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 50, 100, 100, 0],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 50, 100, 100, 0],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 50, 100, 100, 0],
               [titForTat, pavlov, grimTrigger, randomized, 0, 50, 100, 100, 0],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 50, 100, 100, 0],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 100, 100, 0],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 50, 100, 100, 0]]
playerWeights7 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

                #UnilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
playerTypes11 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 50, 100, 0],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 50, 100, 0],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 50, 100, 0],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 50, 100, 0],
               [titForTat, pavlov, grimTrigger, randomized, 0, 50, 100, 0],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 50, 100, 0],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 100, 0],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 50, 100, 0]]
playerWeights11 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

for i in range(11):
    print((((i)/48)*100),"%")
    for bot in playerTypes0:
        bot[6] = i*10
    tournament("3h0: ",0,10,80,playerTypes0, playerWeights0, "CC3DC5CD0DD1", -1, 0, 0)
tournament("3h4: ", 4,10,80,playerTypes4, playerWeights4, "CC3DC5CD0DD1", -1, 0, 0)

for i in range(11):
    print((((i+12)/48)*100),"%")
    for bot in playerTypes1:
        bot[6] = i*10
    tournament("3h1: ",1,10,80,playerTypes1, playerWeights1, "CC3DC5CD0DD1", -1, 0, 0)
tournament("3h5: ", 5,10,80,playerTypes5, playerWeights5, "CC3DC5CD0DD1", -1, 0, 0)

for i in range(11):
    print((((i+23)/48)*100),"%")
    for bot in playerTypes6:
        bot[6] = i*10
    tournament("3h6: ",6,10,80,playerTypes6, playerWeights6, "CC3DC5CD0DD1", -1, 0, 0)
tournament("3h10: ", 10 ,10,80,playerTypes10, playerWeights10, "CC3DC5CD0DD1", -1, 0, 0)

for i in range(11):
    print((((i+34)/48)*100),"%")
    for bot in playerTypes7:
        bot[6] = i*10
    tournament("3h7: ",7,10,80,playerTypes7, playerWeights7, "CC3DC5CD0DD1", -1, 0, 0)
tournament("3h11: ", 11 ,10,80,playerTypes11, playerWeights11, "CC3DC5CD0DD1", -1, 0, 0)
print((((48)/48)*100),"%")

print("H3 Simulation is DONE!")