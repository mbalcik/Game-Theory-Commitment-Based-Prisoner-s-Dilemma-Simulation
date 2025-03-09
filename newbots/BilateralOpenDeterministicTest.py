from bots.BilateralOpenDeterministic import BilateralOpenDeterministic
from game.BilateralOpenDeterministicGame import BilateralOpenDeterministicGame

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
bilateralOpenDeterministicBot1 = BilateralOpenDeterministic(
    titForTat, titForTwoTats, pavlov, grimTrigger, 
    budget=0, 
    coopCommitProb=70, 
    commitType=False,  # Default value for commitType
    opponentCoopCommitType=False  # Default value for opponentCoopCommitType
)

bilateralOpenDeterministicBot2 = BilateralOpenDeterministic(
    titForTat, titForTwoTats, pavlov, alwaysDefect, 
    budget=0, 
    coopCommitProb=80, 
    commitType=False,  # Default value for commitType
    opponentCoopCommitType=False  # Default value for opponentCoopCommitType
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
bilateralOpenDeterministicGame = BilateralOpenDeterministicGame(
    bilateralOpenDeterministicBot1, 
    bilateralOpenDeterministicBot2, 
    bot1PayoffMatrix, 
    bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1
)

# Run the game
bilateralOpenDeterministicGame.gametime()
