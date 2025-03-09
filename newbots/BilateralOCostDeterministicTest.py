from bots.BilateralOCostDeterministic import BilateralOCostDeterministic
from game.BilateralOCostDeterministicGame import BilateralOCostDeterministicGame

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
bilateralOCostDeterministicBot1 = BilateralOCostDeterministic(
    titForTat, titForTwoTats, pavlov, grimTrigger, 
    budget=0, 
    coopCommitProb=70, 
    assumeCommitProb=50, 
    payProb=50, 
    commitType=False,  # Default value for commitType
    opponentCoopCommitType=False  # Default value for opponentCoopCommitType
)

bilateralOCostDeterministicBot2 = BilateralOCostDeterministic(
    titForTat, titForTwoTats, pavlov, alwaysDefect, 
    budget=0, 
    coopCommitProb=80, 
    assumeCommitProb=50, 
    payProb=50, 
    commitType=False,  # Default value for commitType
    opponentCoopCommitType=False  # Default value for opponentCoopCommitType
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
bilateralOCostDeterministicGame = BilateralOCostDeterministicGame(
    bilateralOCostDeterministicBot1, 
    bilateralOCostDeterministicBot2, 
    bot1PayoffMatrix, 
    bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1, 
    observation_cost=3  # Add observation cost parameter
)

# Run the game
bilateralOCostDeterministicGame.gametime()
