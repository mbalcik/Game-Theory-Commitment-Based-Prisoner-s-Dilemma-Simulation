import matplotlib.pyplot as plt
import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='gametheory'
)
cursor = connection.cursor()

# Fetch data for 3h4: tournaments
cursor.execute("""
    SELECT 'Open' AS label, 
           SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
    FROM PLAYERS p
    JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
    JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
    WHERE t.tournament_id LIKE '3h4:%'
    GROUP BY t.tournament_id;
""")
results_3h4 = cursor.fetchall()

# Fetch data for 3h0: tournaments
cursor.execute("""
    SELECT ROUND(AVG(p.assume_commit_prob), 2) AS label, 
           SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
    FROM PLAYERS p
    JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
    JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
    WHERE t.tournament_id LIKE '3h0:%'
    GROUP BY t.tournament_id;
""")
results_3h0 = cursor.fetchall()

cursor.close()
connection.close()

# Process results
labels_3h4, cooperation_rates_3h4 = zip(*results_3h4) if results_3h4 else ([], [])
labels_3h0, cooperation_rates_3h0 = zip(*results_3h0) if results_3h0 else ([], [])

# Convert labels to strings, separating "Open" and numeric labels
labels_3h4 = [str(label) for label in labels_3h4]
numeric_labels_3h0 = sorted([label for label in labels_3h0 if isinstance(label, (int, float))])
labels_3h0_sorted = [str(label) for label in numeric_labels_3h0]

# Combine data for plotting, ensuring "Open" is first and numeric labels follow in order
labels = labels_3h4 + labels_3h0_sorted
cooperation_rates = list(cooperation_rates_3h4) + [
    cooperation_rates_3h0[labels_3h0.index(label)] for label in numeric_labels_3h0
]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(labels, cooperation_rates, color=['yellow'] * len(labels_3h4) + ['blue'] * len(labels_3h0_sorted), alpha=0.7)

# Labels and legend
plt.xlabel('Tournament Type or Bot Assume Commit Rate')
plt.ylabel('Cooperation Rate')
plt.title('Cooperation Rate: Bilateral Deterministic Open vs. Closed With Assume Commit Rates')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()

# Show plot
plt.show()



'''
# Fetch data for 3h10: tournaments
cursor.execute("""
    SELECT 'Open' AS label, 
           SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
    FROM PLAYERS p
    JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
    JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
    WHERE t.tournament_id LIKE '3h10:%'
    GROUP BY t.tournament_id;
""")
results_3h10 = cursor.fetchall()

# Fetch data for 3h6: tournaments
cursor.execute("""
    SELECT ROUND(AVG(p.assume_commit_prob), 2) AS label, 
           SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
    FROM PLAYERS p
    JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
    JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
    WHERE t.tournament_id LIKE '3h6:%'
    GROUP BY t.tournament_id;
""")
results_3h6 = cursor.fetchall()

cursor.close()
connection.close()

# Process results
labels_3h10, cooperation_rates_3h10 = zip(*results_3h10) if results_3h10 else ([], [])
labels_3h6, cooperation_rates_3h6 = zip(*results_3h6) if results_3h6 else ([], [])

# Convert labels to strings, separating "Open" and numeric labels
labels_3h10 = [str(label) for label in labels_3h10]
numeric_labels_3h6 = sorted([label for label in labels_3h6 if isinstance(label, (int, float))])
labels_3h6_sorted = [str(label) for label in numeric_labels_3h6]

# Combine data for plotting, ensuring "Open" is first and numeric labels follow in order
labels = labels_3h10 + labels_3h6_sorted
cooperation_rates = list(cooperation_rates_3h10) + [
    cooperation_rates_3h6[labels_3h6.index(label)] for label in numeric_labels_3h6
]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(labels, cooperation_rates, color=['#FF8C00'] * len(labels_3h10) + ['green'] * len(labels_3h6_sorted), alpha=0.7)

# Labels and legend
plt.xlabel('Tournament Type or Bot Assume Commit Rate')
plt.ylabel('Cooperation Rate')
plt.title('Cooperation Rate: Bilateral Deterministic Open vs. Closed With Assume Commit Rates')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()

# Show plot
plt.show()
'''

