from bots.BilateralOpenMixed import BilateralOpenMixed
from game.BilateralOpenMixedGame import BilateralOpenMixedGame

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
bilateralOpenMixedBot1 = BilateralOpenMixed(
    titForTat, titForTwoTats, pavlov, grimTrigger, 
    budget=0, 
    coopCommitProb=70, 
    opponentCoopCommitProb=50, 
    seed=0  # Default seed value
)

bilateralOpenMixedBot2 = BilateralOpenMixed(
    titForTat, titForTwoTats, pavlov, alwaysDefect, 
    budget=0, 
    coopCommitProb=80, 
    opponentCoopCommitProb=50, 
    seed=0  # Default seed value
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
bilateralOpenMixedGame = BilateralOpenMixedGame(
    bilateralOpenMixedBot1, 
    bilateralOpenMixedBot2, 
    bot1PayoffMatrix, 
    bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1
)

# Run the game
bilateralOpenMixedGame.gametime()
