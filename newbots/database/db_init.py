import mysql.connector
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import csv


db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234", 
  auth_plugin='mysql_native_password'
)
print(db_connection)

# creating database_cursor to perform SQL operation to run queries
db_cursor = db_connection.cursor(buffered=True)

# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE gametheory")

# get list of all databases
db_cursor.execute("SHOW DATABASES")

# print all databases
for db in db_cursor:
    print(db)

db_cursor.execute("USE gametheory")

 # Each table is returned as a tuple

#db_cursor.execute("SHOW TABLES")


#may change size of payoffs
db_cursor.execute("""
CREATE TABLE TOURNAMENTS (
    tournament_id VARCHAR(255) NOT NULL,
    game_type INT,
    game_length INT,
    payoffs VARCHAR(255),
    punishment INT,
    reward INT,
    observation_cost INT,
    PRIMARY KEY (tournament_id)
)
""")

# not used right now, will be used in nested for loops
#insert_tournaments = (
#    "INSERT INTO TOURNAMENTS "
#    "(tournament_id, game_type, game_length, payoffs, punishment, reward) "
#    "VALUES (%s, %s, %s, %s, %s, %s)"
#)

db_cursor.execute("""
CREATE TABLE PLAYERS (
    player_id INT NOT NULL,
    tournament_id VARCHAR(255) NOT NULL,
    most_coop_strat INT,
    less_coop_strat INT,
    less_def_strat INT,
    most_def_strat INT,
    coop_commit_prob FLOAT,
    assume_commit_prob FLOAT,
    pay_prob FLOAT,
    win_count INT,
    draw_count INT,
    loss_count INT,
    budget INT,
    coop_count INT,
    PRIMARY KEY (player_id, tournament_id),
    FOREIGN KEY (tournament_id) REFERENCES TOURNAMENTS(tournament_id)
)
""")

# not used right now, will be used in nested for loops
#insert_players = (
#    "INSERT INTO PLAYERS "
#    "(player_id, most_coop_strat, less_coop_strat, less_def_strat, most_def_strat, coop_comm_prob, assume_comm_prob, pay_prob, win_count, draw_count, loss_count, tour_id) "
#    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#)

db_cursor.execute("""
CREATE TABLE MATCHUPS (
    tournament_id VARCHAR(255) NOT NULL,
    player1_id INT NOT NULL,
    player2_id INT NOT NULL,
    history VARCHAR(255),
    player1_commitment FLOAT,
    player2_commitment FLOAT,
    player1_score INT,
    player2_score INT,
    player1_observed TINYINT,
    player2_observed TINYINT,
    player1_seed_list VARCHAR(255),
    player2_seed_list VARCHAR(255),
    PRIMARY KEY (tournament_id, player1_id, player2_id),
    FOREIGN KEY (tournament_id) REFERENCES TOURNAMENTS(tournament_id),
    FOREIGN KEY (player1_id) REFERENCES PLAYERS(player_id),
    FOREIGN KEY (player2_id) REFERENCES PLAYERS(player_id)
)
""")

# not used right now, will be used in nested for loops
#insert_matchups = (
#    "INSERT INTO MATCHUPS "
#    "(tournament_id, player1_id, player2_id, history, p1_commitment, p2_commitment, p1_score, p2_score, p1_seed_list, p2_seed_list) "
#    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#)

db_cursor.execute("SHOW TABLES")
tables = db_cursor.fetchall()

for table in tables:
    print(table[0]) 