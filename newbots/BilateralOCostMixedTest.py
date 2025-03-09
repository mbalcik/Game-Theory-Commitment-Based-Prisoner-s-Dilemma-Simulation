from bots.BilateralOCostMixed import BilateralOCostMixed
from game.BilateralOCostMixedGame import BilateralOCostMixedGame

from strategies.TitForTat import TitForTat
from strategies.TitForTwoTats import TitForTwoTats
from strategies.Pavlov import Pavlov
from strategies.GrimTrigger import GrimTrigger
from strategies.AlwaysDefect import AlwaysDefect

titForTat = TitForTat()
titForTwoTats = TitForTwoTats()
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect()


bilateralOCostMixedBot1 = BilateralOCostMixed(titForTat, titForTwoTats, pavlov, grimTrigger, 0, 70, 50, 50, 0, 0)
bilateralOCostMixedBot2 = BilateralOCostMixed(titForTat, titForTwoTats, pavlov, alwaysDefect, 0, 80, 50, 50, 0, 0)

bot1PayoffMatrix = {"CC": 3,"DC":5,"CD":0,"DD":1}
bot2PayoffMatrix = {"CC": 3,"DC":5,"CD":0,"DD":1}

bilateralClosedDeterministicGame = BilateralOCostMixedGame(bilateralOCostMixedBot1, bilateralOCostMixedBot2, bot1PayoffMatrix, bot2PayoffMatrix, 7, +1, -1, 3)

bilateralClosedDeterministicGame.gametime()
bilateralClosedDeterministicGame.gametime()