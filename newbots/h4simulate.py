from tournament import tournament

from strategies.TitForTat import TitForTat
from strategies.TitForTwoTats import TitForTwoTats
from strategies.Pavlov import Pavlov
from strategies.GrimTrigger import GrimTrigger
from strategies.AlwaysDefect import AlwaysDefect
from strategies.AlwaysCooperate import AlwaysCooperate
from strategies.GenerousTitForTat import GenerousTitForTat
from strategies.Randomized import Randomized

import itertools

# Instantiate strategy objects
titForTat = TitForTat()
titForTwoTats = TitForTwoTats()
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect()
alwaysCooperate = AlwaysCooperate()
generousTitForTat = GenerousTitForTat()
randomized = Randomized(50)

# Player configurations
playerTypes0 = [
    [pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, False, False],
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, False, False],
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, False, False],
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, False, False],
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, False, False],
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, False, False],
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, False, False],
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, False, False],
]
playerWeights0 = [0.125] * 8

playerTypes2 = [
    [pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, 50, 100, False, False],
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, 50, 100, False, False],
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, 50, 100, False, False],
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, 50, 100, False, False],
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, 50, 100, False, False],
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, 50, 100, False, False],
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, 50, 100, False, False],
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, 50, 100, False, False],
]
playerWeights2 = [0.125] * 8

playerTypes4 = [
    [pavlov, titForTwoTats, titForTat, grimTrigger, 0, 50, False, False],
    [titForTwoTats, titForTat, grimTrigger, alwaysDefect, 0, 50, False, False],
    [pavlov, titForTwoTats, titForTat, alwaysDefect, 0, 50, False, False],
    [alwaysCooperate, pavlov, grimTrigger, alwaysDefect, 0, 50, False, False],
    [alwaysCooperate, pavlov, grimTrigger, randomized, 0, 50, False, False],
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 50, False, False],
    [alwaysCooperate, generousTitForTat, grimTrigger, randomized, 0, 50, False, False],
    [alwaysCooperate, titForTwoTats, grimTrigger, randomized, 0, 50, False, False],
]
playerWeights4 = [0.125] * 8

n = 0
tc = 0

print("0%")

for playerTypes, playerWeights, gameType, id_prefix in [
    (playerTypes0, playerWeights0, 0, "4h0"),
    (playerTypes2, playerWeights2, 2, "4h2"),
    (playerTypes4, playerWeights4, 4, "4h4"),
]:
    for bot_idx in range(len(playerTypes)):
        original_strategies = playerTypes[bot_idx][:4]  # Ensure only strategies are considered
        permutations = list(itertools.permutations(original_strategies))

        for perm in permutations:
            perm_order = ""
            for strategy in perm:
                perm_order += str(original_strategies.index(strategy) + 1)
    
            tournament_id = f"{id_prefix}: {bot_idx}, {perm_order}, "

            playerTypes[bot_idx][:4] = perm  # Apply current permutation
            tournament(
                tournament_id,
                gameType,
                10,
                80,
                playerTypes,
                playerWeights,
                "CC3DC5CD0DD1",
                -1,
                0,
                3,
            )
            tc += 1
            print(f"{(tc / 576) * 100:.2f}%")
        playerTypes[bot_idx][:4] = original_strategies  # Reset strategies

print("All tournaments completed.")