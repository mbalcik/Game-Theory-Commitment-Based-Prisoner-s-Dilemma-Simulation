import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to MySQL database
db_config = {
    'host': 'localhost',          
    'user': 'root',              
    'password': '1234',           
    'database': 'gametheory'      
}

conn = mysql.connector.connect(**db_config)

# Step 2: Query the MATCHUPS table
query = """
SELECT
    tournament_id,
    player1_id,
    player2_id,
    player1_commitment,
    player2_commitment,
    history
FROM MATCHUPS;
"""

matchups_df = pd.read_sql(query, conn)

# Step 3: Close the database connection
conn.close()

# Step 4: Function to calculate cooperation and defection rates
def calculate_rates(history):
    moves = history.replace(" ", "")  # Remove spaces
    c_count = moves.count("C")
    d_count = moves.count("D")
    total_moves = len(moves)
    return c_count / total_moves if total_moves > 0 else 0, d_count / total_moves if total_moves > 0 else 0

# Step 5: Calculate actual cooperation and defection rates
matchups_df["player1_actual_coop"], matchups_df["player1_actual_def"] = zip(*matchups_df["history"].map(calculate_rates))
matchups_df["player2_actual_coop"], matchups_df["player2_actual_def"] = zip(*matchups_df["history"].map(calculate_rates))

# Step 6: Check adherence to stated commitments
matchups_df["player1_obeyed"] = matchups_df.apply(
    lambda row: (row["player1_commitment"] >= 0.5 and row["player1_actual_coop"] >= 0.5) or
                (row["player1_commitment"] < 0.5 and row["player1_actual_def"] >= 0.5),
    axis=1
)
matchups_df["player2_obeyed"] = matchups_df.apply(
    lambda row: (row["player2_commitment"] >= 0.5 and row["player2_actual_coop"] >= 0.5) or
                (row["player2_commitment"] < 0.5 and row["player2_actual_def"] >= 0.5),
    axis=1
)

# Step 7: Aggregate obedience counts
total_obeyed = (matchups_df["player1_obeyed"].sum() + matchups_df["player2_obeyed"].sum())
total_players = 2 * len(matchups_df)  # Each matchup involves two players

total_not_obeyed = total_players - total_obeyed

# Step 8: Create a pie chart
labels = ['Obeyed', 'Did Not Obey']
sizes = [total_obeyed, total_not_obeyed]
colors = ['#4CAF50', '#FF5733']
explode = (0.1, 0)  # Explode the first slice

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Percentage of Players Following Their Commitments")
plt.show()



