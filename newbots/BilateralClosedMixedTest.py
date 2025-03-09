from bots.BilateralClosedMixed import BilateralClosedMixed
from game.BilateralClosedMixedGame import BilateralClosedMixedGame

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
bilateralClosedMixedBot1 = BilateralClosedMixed(
    titForTat, titForTwoTats, pavlov, grimTrigger, 
    budget=0, 
    coopCommitProb=70, 
    assumeCommitProb=50, 
    opponentCommitProb=50, 
    seed=0  # Default seed value
)

bilateralClosedMixedBot2 = BilateralClosedMixed(
    titForTat, titForTwoTats, pavlov, alwaysDefect, 
    budget=0, 
    coopCommitProb=80, 
    assumeCommitProb=50, 
    opponentCommitProb=50, 
    seed=0  # Default seed value
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
bilateralClosedMixedGame = BilateralClosedMixedGame(
    bilateralClosedMixedBot1, 
    bilateralClosedMixedBot2, 
    bot1PayoffMatrix, 
    bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1
)

# Run the game
bilateralClosedMixedGame.gametime()
