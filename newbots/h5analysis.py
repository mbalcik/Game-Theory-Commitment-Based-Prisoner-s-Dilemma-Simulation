from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t, ttest_ind

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'gametheory'
}

# Function to calculate average budgets and confidence intervals
def calculate_average_budgets(players_df, start_id, end_id, interval_index):
    start_ids = range(start_id + (interval_index * 10), end_id, 80)
    average_budgets = []
    confidence_intervals = []
    for start_id in start_ids:
        group_player_ids = range(start_id, start_id + 10)
        group_players = players_df[players_df['player_id'].isin(group_player_ids)]
        group_budgets = group_players['budget']

        avg_budget = group_budgets.mean()

        n = len(group_budgets)
        if n > 1:
            std_err = group_budgets.std() / (n ** 0.5)
            margin_of_error = t.ppf(0.975, df=n - 1) * std_err
            conf_interval = (avg_budget - margin_of_error, avg_budget + margin_of_error)
        else:
            conf_interval = (None, None)

        average_budgets.append((start_id, start_id + 9, avg_budget))
        confidence_intervals.append(conf_interval)
    
    return average_budgets, confidence_intervals

# Define intervals
intervals = [
    (1, 881),
    (881, 1761),
    (1761, 2641),
    (2641, 3521),
    (3521, 4401),
    (4401, 5281),
    (5281, 6161),
    (6161, 7041)
]

colors_5h1 = ['darkblue', 'teal', 'darkorange', 'crimson', 'forestgreen', 'indigo', 'goldenrod', 'green']
colors_5h7 = ['mediumvioletred', 'dodgerblue', 'limegreen', 'darkviolet', 'tomato', 'slateblue', 'darkcyan', 'blue']

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

for idx, (start, end) in enumerate(intervals):
    query_h1 = """
    SELECT * 
    FROM PLAYERS 
    WHERE tournament_id LIKE %s AND player_id BETWEEN %s AND %s
    """
    players_h1_df = pd.read_sql(query_h1, engine, params=('5h1%', start, end))

    query_h7 = """
    SELECT * 
    FROM PLAYERS 
    WHERE tournament_id LIKE %s AND player_id BETWEEN %s AND %s
    """
    players_h7_df = pd.read_sql(query_h7, engine, params=('5h7%', start, end))

    average_budgets_h1, conf_intervals_h1 = calculate_average_budgets(players_h1_df, start, end, idx)
    average_budgets_h7, conf_intervals_h7 = calculate_average_budgets(players_h7_df, start, end, idx)

    groups = [f"{start + (i + idx) * 80}-{start + (i + idx + 1) * 10}" for i in range(len(average_budgets_h1))]
    avg_budgets_h1 = [avg for _, _, avg in average_budgets_h1]
    avg_budgets_h7 = [avg for _, _, avg in average_budgets_h7]

    # Perform t-test for independent samples
    t_stat, p_value = ttest_ind(players_h1_df['budget'], players_h7_df['budget'], equal_var=False)
    print(f"Interval {start}-{end}: T-Stat = {t_stat:.2f}, P-Value = {p_value:.4f}")

    new_x_labels = [i * 10 for i in range(len(groups))]
    x = range(len(groups))
    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    bars_h1 = plt.bar(x, avg_budgets_h1, width=bar_width, label="5h1 Tournaments", color=colors_5h1[idx], align='center')
    bars_h7 = plt.bar([i + bar_width for i in x], avg_budgets_h7, width=bar_width, label="5h7 Tournaments", color=colors_5h7[idx], align='center')

    plt.title(f'Average Budgets for Players in Tournaments ({start}-{end-1})')
    plt.xlabel('Player Groups')
    plt.ylabel('Average Budget')
    plt.xticks(x, new_x_labels, rotation=45)
    plt.legend()

    # Add confidence intervals to bars
    for i, bar in enumerate(bars_h1):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{round(yval, 2)}', va='bottom', ha='center')
        ci = conf_intervals_h1[i]
        if ci[0] is not None:
            plt.errorbar(bar.get_x() + bar.get_width() / 2, yval, yerr=[[yval - ci[0]], [ci[1] - yval]], fmt='o', color='black')

    for i, bar in enumerate(bars_h7):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{round(yval, 2)}', va='bottom', ha='center')
        ci = conf_intervals_h7[i]
        if ci[0] is not None:
            plt.errorbar(bar.get_x() + bar.get_width() / 2, yval, yerr=[[yval - ci[0]], [ci[1] - yval]], fmt='o', color='black')

    plt.tight_layout()
    plt.show()