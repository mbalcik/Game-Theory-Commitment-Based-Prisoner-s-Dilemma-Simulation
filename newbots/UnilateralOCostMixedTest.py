from bots.UnilateralOCostMixed import UnilateralOCostMixed
from game.UnilateralOCostMixedGame import UnilateralOCostMixedGame

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
unilateralOCostMixedBot1 = UnilateralOCostMixed(
    mostCoopStrat=titForTwoTats, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=grimTrigger, 
    budget=0, 
    coopCommitProb=100, 
    payProb=100, 
    opponentCoopCommitProb=0, 
    assumeOppCommitProb=100,
    seed=0  # Default seed value
)

unilateralOCostMixedBot2 = UnilateralOCostMixed(
    mostCoopStrat=alwaysDefect, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=alwaysDefect, 
    budget=0, 
    coopCommitProb=100, 
    payProb=100, 
    opponentCoopCommitProb=0, 
    assumeOppCommitProb=100,
    seed=0  # Default seed value
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
unilateralOCostMixedGame = UnilateralOCostMixedGame(
    bot1=unilateralOCostMixedBot1, 
    bot2=unilateralOCostMixedBot2, 
    bot1PayoffMatrix=bot1PayoffMatrix, 
    bot2PayoffMatrix=bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1, 
    observation_cost=3  # Example value for observation_cost
)

# Run the game
unilateralOCostMixedGame.gametime()

