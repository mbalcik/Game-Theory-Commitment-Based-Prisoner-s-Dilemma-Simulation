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
Bilateral CLosed 1
Bilateral OCost 3
Bilateral Open 5
Uni Closed 7
Uni OCost 9
Uni Open 11

AlwaysCooperate: Cooperativeness Ratio = 1.00
Pavlov: Cooperativeness Ratio = 0.90
TitForTwoTats: Cooperativeness Ratio = 0.84
GenerousTitForTat: Cooperativeness Ratio = 0.83
TitForTat: Cooperativeness Ratio = 0.81
GrimTrigger: Cooperativeness Ratio = 0.75
Randomized: Cooperativeness Ratio = 0.50
AlwaysDefect: Cooperativeness Ratio = 0.00
"""

playerTypes1 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 50, 100, 0, 2],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 50, 100, 0, 1],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 50, 100, 0, 3],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 50, 100, 0, 4],
               [titForTat, pavlov, grimTrigger, randomized, 0, 50, 100, 0, 1],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 50, 100, 0, 3],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 100, 0, 1],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 50, 100, 0, 3]]
playerWeights1 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]



                #BilateralOCostMixed strategies, budget, coopCommitProb, assumeCommitProb, payProb, opponentCoopCommitProb, seed
#playerTypes3 = [[alwaysCooperate, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
#               [pavlov, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
#               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
#               [generousTitForTat, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
#               [titForTat, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
#               [grimTrigger, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
#               [randomized, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
#               [alwaysDefect, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0]]
#playerWeights3 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
#
#for bot in playerTypes3:
#    for i in range(11):
#        bot[5] = i*10
#        tournament("5h3: ",3,10,8,playerTypes3, playerWeights3, "CC3DC5CD0DD1", -1, 0, 3)
#        print("Tournament ended!")
#    bot[5] = 50

                #BilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
#playerTypes5 = [[alwaysCooperate, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#               [pavlov, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#               [generousTitForTat, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#               [titForTat, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#               [grimTrigger, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#               [randomized, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#               [alwaysDefect, titForTat, pavlov, grimTrigger, 0, 100, 100, 0]]
#playerWeights5 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
#
#for bot in playerTypes5:
#    for i in range(11):
#        bot[5] = i*10
#        tournament("5h5: ",5,10,8,playerTypes5, playerWeights5, "CC3DC5CD0DD1", -1, 0, 3)
#        print("Tournament ended!")
#    bot[5] = 50

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

n = 0
print((((n)/16)*100),"%")
for bot_idx in range(len(playerTypes1)):
    n += 1
    print((((n)/16)*100),"%")
    for i in range(11):
        playerTypes1[bot_idx][5] = i*10
        tournament("5h1: " + str(bot_idx) + ", ",1,10,80,playerTypes1, playerWeights1, "CC3DC5CD0DD1", -1, 0, 3)
    playerTypes1[bot_idx][5] = 50

for bot_idx in range(len(playerTypes7)):
    n += 1
    print((((n)/16)*100),"%")
    for i in range(11):
        playerTypes7[bot_idx][5] = i*10
        tournament("5h7: " + str(bot_idx) + ", ",7,10,80,playerTypes7, playerWeights7, "CC3DC5CD0DD1", -1, 0, 3)
    playerTypes7[bot_idx][5] = 50
print("H5 Simulation is DONE!")


                #UnilateralOCostMixed, budget, coopCommitProb, assumeOppCommitProb, payProb, opponentCoopCommitProb, seed
#playerTypes9 = [[alwaysCooperate, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
#               [pavlov, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
#               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
#               [generousTitForTat, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
#               [titForTat, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
#               [grimTrigger, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
#               [randomized, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
#               [alwaysDefect, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1]]
#playerWeights9 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
#
#for bot in playerTypes9:
#    for i in range(11):
#        bot[5] = i*10
#        tournament("5h9: ",9,10,8,playerTypes9, playerWeights9, "CC3DC5CD0DD1", -1, 0, 3)
#        print("Tournament ended!")
#    bot[5] = 50
#
#
#                #UnilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
#playerTypes11 = [[alwaysCooperate, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#                [pavlov, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#                [generousTitForTat, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#                [titForTat, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#                [grimTrigger, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#                [randomized, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
#                [alwaysDefect, titForTat, pavlov, grimTrigger, 0, 100, 100, 0]]
#playerWeights11 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
#
#for bot in playerTypes11:
#    for i in range(11):
#        bot[5] = i*10
#        tournament("5h11: ",11,10,8,playerTypes11, playerWeights11, "CC3DC5CD0DD1", -1, 0, 3)
#        print("Tournament ended!")
#    bot[5] = 50