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




#Bilateral Closed Deterministic = 0, Bilateral Open Deterministic = 4
#strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCommitType
playerTypes0 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 100, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 100, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 100, False, False],  
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 100, False, False],  
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 100, False, False],  
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 100, False, False],  
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 100, False, False],  
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 100, False, False]]

playerWeights0 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]


#Bilateral Closed Mixed = 1, Bilateral Open Mixed = 5
                #BilateralClosedMixed strategies, budget, coopCommitProb, assumeCommitProb, opponentCommitProb, seed
playerTypes1 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 100, 50, 0, 2],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 90, 50, 0, 1],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 84, 50, 0, 3],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 83, 50, 0, 4],
               [titForTat, pavlov, grimTrigger, randomized, 0, 81, 50, 0, 1],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 75, 50, 0, 3],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 0, 1],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 0, 50, 0, 3]]
playerWeights1 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#BilateralOCostDeterministic strategies, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType
playerTypes2 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, 100, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, 100, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, 100, False, False],  
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, 100, False, False],  
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, 100, False, False],  
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 100, False, False],  
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, 100, False, False],  
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, 100, False, False]]

playerWeights2 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

                #BilateralOCostMixed strategies, budget, coopCommitProb, assumeCommitProb, payProb, opponentCoopCommitProb, seed
playerTypes3 = [[alwaysCooperate, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
               [pavlov, titForTat, pavlov, grimTrigger, 0, 90,100,0,0, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 84,100,0,0, 0],
               [generousTitForTat, titForTat, pavlov, grimTrigger, 0, 83,100,0,0, 0],
               [titForTat, titForTat, pavlov, grimTrigger, 0, 81,100,0,0, 0],
               [grimTrigger, titForTat, pavlov, grimTrigger, 0, 75,100,0,0, 0],
               [randomized, titForTat, pavlov, grimTrigger, 0, 50,100,0,0, 0],
               [alwaysDefect, titForTat, pavlov, grimTrigger, 0, 0,100,0,0, 0]]
playerWeights3 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#BilateralOpenDeterministic, strategies, budget, coopCommitProb, commitType, opponentCoopCommitType
playerTypes4 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, False, False],  
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, False, False],  
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, False, False],  
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, False, False],  
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, False, False],  
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, False, False]]

playerWeights4 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

                #BilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
playerTypes5 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 100, 50, 2],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 90, 50, 1],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 84, 50, 3],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 83, 50, 4],
               [titForTat, pavlov, grimTrigger, randomized, 0, 81, 50, 1],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 75, 50, 3],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 1],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 0, 50, 3]]
playerWeights5 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]


#UnilateralClosedDeterministic, strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType
playerTypes6 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, False, False],  
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, False, False],  
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, False, False],  
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, False, False],  
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, False, False],  
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, False, False]]

playerWeights6 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#Unilateral Closed Mixed = 7, Unilateral Open Mixed = 11
                #UnilateralClosedMixed, strategies, budget, coopCommitProb, assumeOpponentCommitProb, opponentCoopCommitProb, seed
playerTypes7 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 100, 100, 100, 0],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 90, 100, 100, 0],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 84, 100, 100, 0],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 83, 100, 100, 0],
               [titForTat, pavlov, grimTrigger, randomized, 0, 81, 100, 100, 0],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 75, 100, 100, 0],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 100, 100, 0],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 0, 100, 100, 0]]
playerWeights7 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#UnilateralOCostDeterministic, strategies, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType
playerTypes8 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, 100, True, False],  
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, 100, True, False],  
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, 100, True, False],  
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, 100, True, False],  
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, 100, True, False],  
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 100, True, False],  
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, 100, True, False],  
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, 100, True, False]]

playerWeights8 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#UnilateralOCostMixed, strategies, budget, coopCommitProb, assumeOppCommitProb, payProb, opponentCoopCommitProb, seed
playerTypes9 = [[alwaysCooperate, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
               [pavlov, titForTat, pavlov, grimTrigger, 0, 90, 100, 100, 100, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 84, 100, 100, 100, 1],
               [generousTitForTat, titForTat, pavlov, grimTrigger, 0, 83, 100, 100, 100, 1],
               [titForTat, titForTat, pavlov, grimTrigger, 0, 81, 100, 100, 100, 1],
               [grimTrigger, titForTat, pavlov, grimTrigger, 0, 75, 100, 100, 100, 1],
               [randomized, titForTat, pavlov, grimTrigger, 0, 50, 100, 100, 100, 1],
               [alwaysDefect, titForTat, pavlov, grimTrigger, 0, 0, 100, 100, 100, 1]]
playerWeights9 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

#UnilateralOpenDeterministic, budget, coopCommitProb, commitType, opponentCoopCommitType
playerTypes10 = [[pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, False, False],  
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, False, False],  
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, False, False],  
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, False, False],  
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, False, False],  
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, False, False],  
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, False, False]]

playerWeights10 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]


                #UnilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
playerTypes11 = [[alwaysCooperate, titForTwoTats, titForTat, grimTrigger, 0, 100, 100, 0],
               [pavlov, titForTat, grimTrigger, alwaysDefect, 0, 90, 100, 0],
               [titForTwoTats, titForTwoTats, titForTat, alwaysDefect, 0, 84, 100, 0],
               [generousTitForTat, pavlov, grimTrigger, alwaysDefect, 0, 83, 100, 0],
               [titForTat, pavlov, grimTrigger, randomized, 0, 81, 100, 0],
               [grimTrigger, titForTat, grimTrigger, randomized, 0, 75, 100, 0],
               [randomized, generousTitForTat, grimTrigger, randomized, 0, 50, 100, 0],
               [alwaysDefect, titForTwoTats, grimTrigger, randomized, 0, 0, 100, 0]]
playerWeights11 = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
    

def listOfTournament(i):
    # Ensure i is within the valid range
    if i < 0 or i > 11:
        raise ValueError("Invalid index. Please provide an index between 0 and 11.")

    # Define playerTypes and playerWeights for each index
    # Assuming all types and weights are defined elsewhere in the code
    playerTypes = {
        0: playerTypes0,
        1: playerTypes1,  # Assuming playerTypes1 is defined
        2: playerTypes2,
        3: playerTypes3,  # Assuming playerTypes3 is defined
        4: playerTypes4,
        5: playerTypes5,  # Assuming playerTypes5 is defined
        6: playerTypes6,
        7: playerTypes7,  # Assuming playerTypes7 is defined
        8: playerTypes8,
        9: playerTypes9,  # Assuming playerTypes9 is defined
        10: playerTypes10,
        11: playerTypes11  # Assuming playerTypes11 is defined
    }

    playerWeights = {
        0: playerWeights0,
        1: playerWeights1,  # Assuming playerWeights1 is defined
        2: playerWeights2,
        3: playerWeights3,  # Assuming playerWeights3 is defined
        4: playerWeights4,
        5: playerWeights5,  # Assuming playerWeights5 is defined
        6: playerWeights6,
        7: playerWeights7,  # Assuming playerWeights7 is defined
        8: playerWeights8,
        9: playerWeights9,  # Assuming playerWeights9 is defined
        10: playerWeights10,
        11: playerWeights11  # Assuming playerWeights11 is defined
    }

    # Return the corresponding playerTypes and playerWeights
    return playerTypes[i], playerWeights[i]
    

for i in range(12):
    tour_str1 = "7h1: " + str(i) 
    tour_str2 = "7h2: " + str(i)

    playerTypes = listOfTournament(i)[0]
    playerWeights = listOfTournament(i)[1]

    tournament(tour_str1,i,7,80,playerTypes, playerWeights, "CC3DC5CD0DD1", -1, 0, 3)
    tournament(tour_str2,i,7,80,playerTypes, playerWeights, "CC3DC5CD0DD1", -10, 0, 3)
    print("tournament "+ str(i)+" done!")