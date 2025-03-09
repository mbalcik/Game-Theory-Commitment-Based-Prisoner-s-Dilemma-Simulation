from bots.UnilateralOpenMixed import UnilateralOpenMixed
from game.UnilateralOpenMixedGame import UnilateralOpenMixedGame

from strategies.TitForTat import TitForTat
from strategies.TitForTwoTats import TitForTwoTats
from strategies.Pavlov import Pavlov
from strategies.GrimTrigger import GrimTrigger
from strategies.AlwaysDefect import AlwaysDefect

# Define strategies
titForTat = TitForTat()
titForTwoTats = TitForTwoTats()
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect()

# Create bot instances
unilateralOCostMixedBot1 = UnilateralOpenMixed(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=grimTrigger, 
    budget=0, 
    coopCommitProb=70, 
    opponentCoopCommitProb=0, 
    seed=0  # Default seed value
)

unilateralOCostMixedBot2 = UnilateralOpenMixed(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=alwaysDefect, 
    budget=0, 
    coopCommitProb=80, 
    opponentCoopCommitProb=0, 
    seed=0  # Default seed value
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
unilateralOCostMixedGame = UnilateralOpenMixedGame(
    bot1=unilateralOCostMixedBot1, 
    bot2=unilateralOCostMixedBot2, 
    bot1PayoffMatrix=bot1PayoffMatrix, 
    bot2PayoffMatrix=bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1,
)

# Run the game
unilateralOCostMixedGame.gametime()
unilateralOCostMixedGame.gametime()
