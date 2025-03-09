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

"""
Bilateral CLosed Deterministic 0
Bilateral OCost Deterministic 2
Bilateral Open Deterministic 4
Uni Closed Deterministic 6
Uni OCost Deterministic 8
Uni Open Deterministic 10

Bilateral Closed Mixed 1
Unilateral Closed Mixed 7
"""
 #BilateralClosedDeterministic strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCommitType
playerTypes0 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, False, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, False, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, False, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, False, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, False, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, False, False]]
playerWeights0 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#BilateralOCostDeterministic strategies, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType
playerTypes2 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, 100, False, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, 100, False, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, 100, False, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, 100, False, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, 100, False, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, 100, False, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 100, False, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, 100, False, False]]
playerWeights2 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

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

#UnilateralClosedDeterministic, strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType
playerTypes6 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, False, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, False, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, False, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, False, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, False, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, False, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, False, False]]
playerWeights6 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#UnilateralOCostDeterministic, strategies, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType
playerTypes8 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, 100, True, False],
               [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, 100, True, False],
               [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, 100, True, False],
               [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, 100, True, False],
               [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, 100, True, False],
               [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, 100, True, False],
               [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 100, True, False],
               [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, 100, True, False]]
playerWeights8 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

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



#MIXED!
#BilateralClosedMixed strategies, budget, coopCommitProb, assumeCommitProb, opponentCommitProb, seed
playerTypes1 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, 0, 2],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, 0, 1],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, 0, 3],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, 0, 4],
               [titForTat, pavlov, grimTrigger, randomized, 0, 50, 50, 0, 1],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 50, 50, 0, 3],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 0, 1],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 50, 50, 0, 3]]
playerWeights1 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#UnilateralClosedMixed, strategies, budget, coopCommitProb, assumeOpponentCommitProb, opponentCoopCommitProb, seed
playerTypes7 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, 100, 0],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, 100, 0],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, 100, 0],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, 100, 0],
               [titForTat, pavlov, grimTrigger, randomized, 0, 50, 50, 100, 0],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 50, 50, 100, 0],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 100, 0],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 50, 50, 100, 0]]
playerWeights7 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

n = 0
print((((n)/8)*100),"%")
tournament("6h0: ",0,10,80,playerTypes0, playerWeights0, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")
tournament("6h1: ",1,10,80,playerTypes1, playerWeights1, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")
tournament("6h2: ",2,10,80,playerTypes2, playerWeights2, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")

tournament("6h4: ",4,10,80,playerTypes4, playerWeights4, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")

tournament("6h6: ",6,10,80,playerTypes6, playerWeights6, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")

tournament("6h7: ",7,10,80,playerTypes7, playerWeights7, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")

tournament("6h8: ",8,10,80,playerTypes8, playerWeights8, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")

tournament("6h10: ",10,10,80,playerTypes10, playerWeights10, "CC3DC5CD0DD1", -1, 0, 3)
n+=1
print((((n)/8)*100),"%")

print("H6 Simulation is DONE!")