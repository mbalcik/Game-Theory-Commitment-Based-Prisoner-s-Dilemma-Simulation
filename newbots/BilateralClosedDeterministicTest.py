import time
from bots.BilateralClosedDeterministic import BilateralClosedDeterministic
from game.BilateralClosedDeterministicGame import BilateralClosedDeterministicGame

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
bilateralClosedDeterministicBot1 = BilateralClosedDeterministic(
    alwaysDefect, alwaysDefect, alwaysDefect, alwaysDefect, 
    budget=0, 
    coopCommitProb=70, 
    assumeCommitProb=50, 
    commitType=False, 
    opponentCoopCommitType=False
)

bilateralClosedDeterministicBot2 = BilateralClosedDeterministic(
    titForTat, titForTwoTats, pavlov, alwaysDefect, 
    budget=0, 
    coopCommitProb=80, 
    assumeCommitProb=50, 
    commitType=False, 
    opponentCoopCommitType=False
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
bilateralClosedDeterministicGame = BilateralClosedDeterministicGame(
    bilateralClosedDeterministicBot1, 
    bilateralClosedDeterministicBot2, 
    bot1PayoffMatrix, 
    bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1
)

# Measure execution time
start_time = time.time()
bilateralClosedDeterministicGame.gametime()
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"gametime execution took {elapsed_time:.4f} seconds")

# Output matchup info
print(bilateralClosedDeterministicGame.sendMatchupInfo())
