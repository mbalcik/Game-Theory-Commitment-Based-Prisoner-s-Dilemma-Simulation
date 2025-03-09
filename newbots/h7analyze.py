import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'gametheory'
}

def plot_average_rankings(base_tournament_id):
    # Define tournament type mappings
    tournament_types = {
        0: "Bilateral Closed Deterministic",
        1: "Bilateral Closed Mixed",
        2: "Bilateral Observation Cost Deterministic",
        3: "Bilateral Observation Cost Mixed",
        4: "Bilateral Open Deterministic",
        5: "Bilateral Open Mixed",
        6: "Unilateral Closed Deterministic",
        7: "Unilateral Closed Mixed",
        8: "Unilateral Observation Cost Deterministic",
        9: "Unilateral Observation Cost Mixed",
        10: "Unilateral Open Deterministic",
        11: "Unilateral Open Mixed"
    }

    # Get the tournament name from the mapping
    tournament_name = tournament_types.get(base_tournament_id, "Unknown Tournament")

    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Define tournament IDs for 7h1 and 7h2
    tournament_7h1 = f"7h1: {base_tournament_id}"
    tournament_7h2 = f"7h2: {base_tournament_id}"

    # Retrieve players for 7h1
    cursor.execute("""
        SELECT player_id, budget 
        FROM players 
        WHERE tournament_id = %s 
        ORDER BY budget DESC
    """, (tournament_7h1,))
    players_7h1 = cursor.fetchall()

    # Retrieve players for 7h2
    cursor.execute("""
        SELECT player_id, budget 
        FROM players 
        WHERE tournament_id = %s 
        ORDER BY budget DESC
    """, (tournament_7h2,))
    players_7h2 = cursor.fetchall()

    # Helper function to assign player types
    def assign_player_types(players):
        player_types = {}
        for player_id, budget in players:
            player_type = (player_id - 1) // 10 + 1
            if player_type not in player_types:
                player_types[player_type] = []
            player_types[player_type].append((player_id, budget))
        return player_types

    # Assign player types for both tournaments
    player_types_7h1 = assign_player_types(players_7h1)
    player_types_7h2 = assign_player_types(players_7h2)

    # Calculate rankings for each player
    rankings_7h1 = {player_id: rank + 1 for rank, (player_id, budget) in enumerate(players_7h1)}
    rankings_7h2 = {player_id: rank + 1 for rank, (player_id, budget) in enumerate(players_7h2)}

    # Calculate average rankings for each player type
    average_rankings_7h1 = []
    average_rankings_7h2 = []

    max_player_type = max(
        max(player_types_7h1.keys(), default=0),
        max(player_types_7h2.keys(), default=0),
    ) // 2

    for player_type in range(1, max_player_type + 1):
        type_rankings_7h1 = [rankings_7h1[player_id] for player_id, _ in player_types_7h1.get(player_type, [])]
        type_rankings_7h2 = [rankings_7h2[player_id] for player_id, _ in player_types_7h2.get(player_type + max_player_type, [])]

        avg_7h1 = sum(type_rankings_7h1) / len(type_rankings_7h1) if type_rankings_7h1 else 0
        avg_7h2 = sum(type_rankings_7h2) / len(type_rankings_7h2) if type_rankings_7h2 else 0

        average_rankings_7h1.append(avg_7h1)
        average_rankings_7h2.append(avg_7h2)

    # Prepare data for plotting
    x = np.arange(1, max_player_type + 1)
    width = 0.35

    # Plotting the bar graph
    fig, ax = plt.subplots()
    ax.bar(x - width / 2, average_rankings_7h1, width, label='-1 Punishment (7h1)')
    ax.bar(x + width / 2, average_rankings_7h2, width, label='-10 Punishment (7h2)')

    # Adding labels, title, and legend
    ax.set_xlabel('Player Types')
    ax.set_ylabel('Average Rankings')
    ax.set_title(f"Average Rankings for Bot Types in {tournament_name} with -1 and -10 Punishment")
    ax.set_xticks(x)
    ax.set_xticklabels(x)
    ax.legend()

    plt.show()

    # Close the database connection
    conn.close()

# Example usage
# plot_average_rankings(10)  # Replace with the base tournament ID


for i in (1,3,5,7,9,11):
    # Example usage
    plot_average_rankings(i)  # Replace with the base tournament ID
