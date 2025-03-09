from tournament import tournament
from strategies.TitForTat import TitForTat
from strategies.TitForTwoTats import TitForTwoTats
from strategies.Pavlov import Pavlov
from strategies.GrimTrigger import GrimTrigger
from strategies.AlwaysDefect import AlwaysDefect
from strategies.AlwaysCooperate import AlwaysCooperate
from strategies.GenerousTitForTat import GenerousTitForTat
from strategies.Randomized import Randomized

# Define strategies
titForTat = TitForTat()
titForTwoTats = TitForTwoTats()
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect()
alwaysCooperate = AlwaysCooperate()
generousTitForTat = GenerousTitForTat()
randomized = Randomized(50)

# Custom bot behavior for alignment with analysis
playerTypesCustom = [
    # Always obey commitments
    [alwaysCooperate, titForTat, grimTrigger, randomized, 0, 70, 70, True, False, False],
    # Sometimes obey commitments based on randomness
    [pavlov, titForTwoTats, grimTrigger, alwaysDefect, 0, 50, 50, True, True, False],
    # Rarely obey commitments (mostly defect)
    [alwaysDefect, pavlov, grimTrigger, randomized, 0, 30, 30, False, False, False],
    # Moderate alignment with a mix of strategies
    [generousTitForTat, titForTat, titForTwoTats, randomized, 0, 60, 60, True, True, False],
]

playerWeightsCustom = [0.25, 0.25, 0.25, 0.25]

# Debug: Verify player types structure
for i, playerType in enumerate(playerTypesCustom):
    print(f"Player Type {i}: {playerType}")

# Run the simulation with custom bots
print("Starting Custom Simulation...")
n = 0

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim0: ", 0, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim1: ", 1, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim2: ", 2, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim3: ", 3, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim4: ", 4, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim5: ", 5, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim6: ", 6, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print(f"{((n)/8)*100:.1f} % completed")
tournament("CustomSim7: ", 7, 10, 80, playerTypesCustom, playerWeightsCustom, "CC3DC5CD0DD1", -1, 0, 3)
n += 1

print("Custom Simulation is DONE!")
