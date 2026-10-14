#### RPI Men's Club Soccer Rating Calculator ####
#### Test script ####

## TODO: add protection against booleans being considered as integers
## when calculating a player's rating (True = 1, False = 0)

def calculate_player_rating(player):
    position = player["position"]
    rating = 6.0 # Base rating for all players
    
    # Goalkeeper rating calculation
    if position == "Goalkeeper":
        saves = player.get("saves", 0) 
        goals_conceded = player.get("goals_conceded", 0)
        
        score = rating + (saves * 0.15) - (goals_conceded * 0.4)
    elif position == "Defender":
        goals = player.get("goals", 0)
        assists = player.get("assists", 0)
        tackles_won = player.get("tackles_won", 0)
        tackles_lost = player.get("tackles_lost", 0)
        
        score = rating + goals + (assists * 0.6) + (tackles_won * 0.05) - (tackles_lost * 0.05)
    elif position == "Midfielder":
        goals = player.get("goals", 0)
        assists = player.get("assists", 0)
        tackles_won = player.get("tackles_won", 0)
        tackles_lost = player.get("tackles_lost", 0)
        
        score = rating + (goals * 0.8) + (assists * 0.5) + (tackles_won * 0.08) - (tackles_lost * 0.04)
    elif position == "Forward":
        goals = player.get("goals", 0)
        assists = player.get("assists", 0)
        tackles_won = player.get("tackles_won", 0)
        tackles_lost = player.get("tackles_lost", 0)
        
        score = rating + (goals * 0.6) + (assists * 0.4) + (tackles_won * 0.1) - (tackles_lost * 0.05)
    else:
        return 0
    return balance_rating(score)
    
def balance_rating(score):
    if score < 0:
        return 0
    elif score > 10:
        return 10
    else:
        return score
