from bots.UnilateralOCostDeterministic import UnilateralOCostDeterministic
from game.UnilateralOCostDeterministicGame import UnilateralOCostDeterministicGame

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
unilateralOCostDeterministicBot1 = UnilateralOCostDeterministic(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=grimTrigger, 
    budget=0, 
    coopCommitProb=50, 
    assumeCommitProb=50, 
    payProb=50, 
    commitType=True,  # Example value for commitType
    opponentCoopCommitType=False  # Example value for opponentCoopCommitType
)

unilateralOCostDeterministicBot2 = UnilateralOCostDeterministic(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=alwaysDefect, 
    budget=0, 
    coopCommitProb=50, 
    assumeCommitProb=50, 
    payProb=50, 
    commitType=False,  # Example value for commitType
    opponentCoopCommitType=True  # Example value for opponentCoopCommitType
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
unilateralOCostDeterministicGame = UnilateralOCostDeterministicGame(
    bot1=unilateralOCostDeterministicBot1, 
    bot2=unilateralOCostDeterministicBot2, 
    bot1PayoffMatrix=bot1PayoffMatrix, 
    bot2PayoffMatrix=bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1, 
    observation_cost=3  # Example value for observation_cost
)

# Run the game
unilateralOCostDeterministicGame.gametime()
