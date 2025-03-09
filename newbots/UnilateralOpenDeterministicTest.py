from bots.UnilateralOpenDeterministic import UnilateralOpenDeterministic
from game.UnilateralOpenDeterministicGame import UnilateralOpenDeterministicGame

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
unilateralOpenDeterministicBot1 = UnilateralOpenDeterministic(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=grimTrigger, 
    budget=0, 
    coopCommitProb=50, 
    commitType=True,  # True as a default value, can change
    opponentCoopCommitType=True  # True as a default value, can change
)

unilateralOpenDeterministicBot2 = UnilateralOpenDeterministic(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=alwaysDefect, 
    budget=0, 
    coopCommitProb=50, 
    commitType=False,  # False as a default value
    opponentCoopCommitType=True  # True as a default value
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
unilateralOpenDeterministicGame = UnilateralOpenDeterministicGame(
    bot1=unilateralOpenDeterministicBot1, 
    bot2=unilateralOpenDeterministicBot2, 
    bot1PayoffMatrix=bot1PayoffMatrix, 
    bot2PayoffMatrix=bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1  # Example values for commitment and punishment
)

# Run the game
unilateralOpenDeterministicGame.gametime()
