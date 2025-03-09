import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, sem
import numpy as np

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="gametheory"
)

db_cursor = connection.cursor()

# List of tournament pairs with new titles
tournament_pairs = [
    ("6h0:", "6h6:", "Bilateral Closed Deterministic", "Unilateral Closed Deterministic"),
    ("6h1:", "6h7:", "Mixed", "Mixed"),
    ("6h2:", "6h8:", "Bilateral OCost Deterministic", "Unilateral OCost Deterministic"),
    ("6h4:", "6h10:", "Bilateral Open Deterministic", "Unilateral Open Deterministic")
]

for prefix1, prefix2, title1, title2 in tournament_pairs:
    # Query the data for the first prefix
    query1 = f"""
    SELECT player_id, budget, tournament_id
    FROM PLAYERS
    WHERE tournament_id LIKE '{prefix1}%'
    """
    db_cursor.execute(query1)
    data1 = pd.DataFrame(db_cursor.fetchall(), columns=['player_id', 'budget', 'tournament_id'])

    # Query the data for the second prefix
    query2 = f"""
    SELECT player_id, budget, tournament_id
    FROM PLAYERS
    WHERE tournament_id LIKE '{prefix2}%'
    """
    db_cursor.execute(query2)
    data2 = pd.DataFrame(db_cursor.fetchall(), columns=['player_id', 'budget', 'tournament_id'])

    # Process data for both prefixes
    def process_data(data):
        if data.empty:
            return None
        data = data.sort_values(by=['budget'], ascending=False).reset_index(drop=True)
        data['rank'] = data.index + 1
        data['player_type'] = (data['player_id'] - 1) // 10
        avg_ranking = data.groupby('player_type')['rank'].mean().reset_index()
        return avg_ranking

    avg_ranking1 = process_data(data1)
    avg_ranking2 = process_data(data2)

    if avg_ranking1 is None or avg_ranking2 is None:
        print(f"No data found for pair {title1} and {title2}")
        continue

    # Perform t-test and compute confidence interval
    combined_types = set(avg_ranking1['player_type']).intersection(set(avg_ranking2['player_type']))
    ranks1 = avg_ranking1[avg_ranking1['player_type'].isin(combined_types)]['rank'].values
    ranks2 = avg_ranking2[avg_ranking2['player_type'].isin(combined_types)]['rank'].values

    t_stat, p_value = ttest_ind(ranks1, ranks2, equal_var=False)  # Welch's t-test for unequal variance
    confidence_level = 0.95
    n1, n2 = len(ranks1), len(ranks2)
    se_diff = np.sqrt(sem(ranks1)**2 + sem(ranks2)**2)
    margin_of_error = se_diff * 1.96  # 1.96 for 95% confidence level
    mean_diff = ranks1.mean() - ranks2.mean()
    ci_low, ci_high = mean_diff - margin_of_error, mean_diff + margin_of_error

    # Print statistics
    print(f"\nComparison: {title1} vs {title2}")
    print(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")
    print(f"Mean difference: {mean_diff:.2f}")
    print(f"95% Confidence Interval: ({ci_low:.2f}, {ci_high:.2f})")

    # Print rankings and sums
    print(f"Average Rankings for {title1}:")
    print(avg_ranking1)
    print(f"Sum for {title1}: {avg_ranking1['rank'].sum()}")

    print(f"Average Rankings for {title2}:")
    print(avg_ranking2)
    print(f"Sum for {title2}: {avg_ranking2['rank'].sum()}")

    # Plot the data for both prefixes
    plt.figure(figsize=(10, 6))
    bars1 = plt.bar(avg_ranking1['player_type'] - 0.2, avg_ranking1['rank'], width=0.4, label=title1, color='crimson')
    bars2 = plt.bar(avg_ranking2['player_type'] + 0.2, avg_ranking2['rank'], width=0.4, label=title2, color='gold')

    plt.xlabel('Player Type')
    plt.ylabel('Average Placing')
    plt.title(f'Average Placing by Player Type - {title1} vs {title2}')
    plt.xticks(avg_ranking1['player_type'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    # Annotate bars with exact values
    for bars in [bars1, bars2]:
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}', ha='center', va='bottom')

    plt.show()

# Close database connection
db_cursor.close()
connection.close()
