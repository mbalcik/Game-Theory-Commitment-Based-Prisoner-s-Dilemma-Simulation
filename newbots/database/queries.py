insertTournament = """INSERT INTO tournaments (tournament_id, game_type, game_length, payoffs, punishment, reward, observation_cost) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

insertPlayer = """INSERT INTO players 
                (player_id, tournament_id, most_coop_strat, less_coop_strat, less_def_strat, most_def_strat, 
                coop_commit_prob, assume_commit_prob, pay_prob, win_count, draw_count, loss_count, budget, coop_count)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

insertMatchup = """INSERT INTO matchups 
                    (tournament_id, player1_id, player2_id, history, player1_commitment, player2_commitment, player1_score, player2_score, player1_observed, player2_observed, player1_seed_list, player2_seed_list)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

updateBudget = """UPDATE players 
                                    SET budget = %s 
                                    WHERE player_id = %s AND tournament_id = %s"""

getWins = """SELECT win_count
                FROM players
                WHERE player_id = %s AND tournament_id = %s"""
                    
getDraws = """SELECT draw_count 
                FROM players
                WHERE player_id = %s AND tournament_id = %s"""
                    
getLosses = """SELECT loss_count 
                FROM players
                WHERE player_id = %s AND tournament_id = %s"""
                    
updateWins = """UPDATE players 
                SET win_count = %s 
                WHERE player_id = %s AND tournament_id = %s"""
                    
updateDraws = """UPDATE players 
                SET draw_count = %s 
                WHERE player_id = %s AND tournament_id = %s"""
                    
updateLosses = """UPDATE players 
                SET loss_count = %s 
                WHERE player_id = %s AND tournament_id = %s"""

updateCoopCount = """UPDATE players 
                SET coop_count = %s 
                WHERE player_id = %s AND tournament_id = %s"""