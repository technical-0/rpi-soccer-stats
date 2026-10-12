#### RPI Men's Club Soccer Team Stats Analysis ####
#### Test script ####

### Function to initialize the stats for each position
def initialize_positions(position, positions):
    main_positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
    try:
        if position not in main_positions:
            raise ValueError
    except ValueError:
        print(f"Error: Position {position} is not a valid position. Valid positions are: {', '.join(main_positions)}")
        return False
    else:
        print(f"Position {position} is valid. Initializing stats for {position}...")
        if position == "Goalkeeper":
            if position not in positions:
                positions[position] = {
                    "player_count": 0,
                    "saves": 0,
                    "goals_conceded": 0,
                }
        else:
            if position not in positions:
                positions[position] = {
                    "player_count": 0,
                    "goals": 0,
                    "assists": 0,
                    "tackles_won": 0,
                    "tackles_lost": 0,
                }
        print("Done!")
        return True
        

### Function to add player stats to the positions dictionary
def add_player_stats(player, positions, duplicates):
    position = player["position"]
    name = player["name"]
    gk_count = 0
    position_count = 0
    if name in duplicates:
        print(f"Error: Duplicate player name found: {name}. Skipping this player.")
        return
    else:
        duplicates.add(name)
    
    if position == "Goalkeeper":
        ## Check for negative statistics and handle them
        # Saves
        if type(player.get("saves", 0)) != int or player.get("saves", 0) < 0:
            print(f"Warning: Invalid statistic found for player {name} in position {position}. Skipping 'saves'.")
            gk_count += 1
        else:
            positions[position]["saves"] += player.get("saves", 0)
        
        # Goals Conceded
        if type(player.get("goals_conceded", 0)) != int  or player.get("goals_conceded", 0) < 0:
            print(f"Warning: Invalid statistic found for player {name} in position {position}. Skipping 'goals_conceded'.")
            gk_count += 1
        else:
            positions[position]["goals_conceded"] += player.get("goals_conceded", 0)
        
        # Checks if all statistics for the goalkeeper are invalid
        if gk_count == 2:
            print(f"Error: All statistics for player {name} in position {position} are invalid. Skipping this player.")
            duplicates.remove(name) # Remove the player from duplicates set since they were skipped
        else:
            positions[position]["player_count"] += 1
    else:
        ## Check for negative statistics and handle them
        # Goals
        if type(player.get("goals", 0)) != int  or player.get("goals", 0) < 0:
            print(f"Warning: Invalid statistic found for player {name} in position {position}. Skipping 'goals'.")
            position_count += 1
        else:
            positions[position]["goals"] += player.get("goals", 0)
        
        # Assists
        if type(player.get("assists", 0)) != int or player.get("assists", 0) < 0:
            print(f"Warning: Invalid statistic found for player {name} in position {position}. Skipping 'assists'.")
            position_count += 1
        else:
            positions[position]["assists"] += player.get("assists", 0)
        
        # Tackles Won
        if type(player.get("tackles_won", 0)) != int or player.get("tackles_won", 0) < 0:
            print(f"Warning: Invalid statistic found for player {name} in position {position}. Skipping 'tackles_won'.")
            position_count += 1
        else:
            positions[position]["tackles_won"] += player.get("tackles_won", 0)
        
        # Tackles Lost
        if type(player.get("tackles_lost", 0)) != int or player.get("tackles_lost", 0) < 0:
            print(f"Warning: Invalid statistic found for player {name} in position {position}. Skipping 'tackles_lost'.")
            position_count += 1
        else:
            positions[position]["tackles_lost"] += player.get("tackles_lost", 0)

        # Check if all statistics for the player are invalid
        if position_count == 4:
            print(f"Error: All statistics for player {name} in position {position} are invalid. Skipping this player.")
            duplicates.remove(name) # Remove the player from duplicates set since they were skipped
        else:
            positions[position]["player_count"] += 1
        
### Fake data for testing purposes
players = [
    {"name": "Fake Player #1", 
         "position": "Forward",
         "goals": -3,
         "assists": 1,
         "tackles_won": 0,
         "tackles_lost": 0,
        },
        
        {"name": "Fake Player #2", 
         "position": "Midfielder",
         "goals": 1,
         "assists": 3,
         "tackles_won": -1,
         "tackles_lost": 3,
        },
        
        {"name": "Fake Player #3", 
         "position": "Defender",
         "goals": 1,
         "assists": -2,
         "tackles_won": 9,
         "tackles_lost": 1,
        },
        
        {"name": "Fake Player #4", 
         "position": "Goalkeeper",
         "saves": 5,
         "goals_conceded": 1,
        },
        
        {"name": "Fake Player #4", 
         "position": "Goalkeper",
         "saves": 5,
         "goals_conceded": 1,
        },
        
        {"name": "Fake Player #5", 
         "position": "Defender",
         "goals": 0,
         "tackles_won": 3,
         "tackles_lost": -3,
        },
        
        {"name": "Fake Player #6", 
         "position": "Midfielder",
         "goals": True,
         "assists": False,
         "tackles_won": True,
         "tackles_lost": False,
        }
]

### Initialize the positions dictionary to store stats for each position
positions = {}
duplicates = set()
for player in players:
    position = player["position"] 
    valid = initialize_positions(position, positions)
    if valid:
        add_player_stats(player, positions, duplicates)
    
## Display the stats for each position
if not positions:
    print("No valid players found")

for position, stats in positions.items():
    print(f"Position: {position}")
    print(f"Player Count: {stats['player_count']}")
    
    if position == "Goalkeeper":
        print(f"Saves: {stats['saves']}")
        print(f"Goals Conceded: {stats['goals_conceded']}")
    else:
        print(f"Goals: {stats['goals']}")
        print(f"Assists: {stats['assists']}")
        print(f"Tackles Won: {stats['tackles_won']}")
        print(f"Tackles Lost: {stats['tackles_lost']}")
        total_tackles = stats['tackles_won'] + stats['tackles_lost']
        if total_tackles > 0:
            tackle_success_rate = (stats['tackles_won'] / total_tackles) * 100
            print(f"Tackle Success Rate: {tackle_success_rate:.2f}%")
        else:
            print("Tackle Success Rate: N/A")
    print()