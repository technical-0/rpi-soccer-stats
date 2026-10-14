#### Main Script for Analysis ####
#### Test script ####
from analyze_stats import initialize_positions, add_player_stats, display_stats
from calculate_ratings import calculate_player_rating

### Fake data for testing purposes
players = [
    {"name": "Fake Player #1", 
         "position": "Forward",
         "goals": 3,
         "assists": 1,
         "tackles_won": 0,
         "tackles_lost": 0,
        },
        
        {"name": "Fake Player #2", 
         "position": "Midfielder",
         "goals": 1,
         "assists": 3,
         "tackles_won": 1,
         "tackles_lost": 3,
        },
        
        {"name": "Fake Player #3", 
         "position": "Defender",
         "goals": 1,
         "assists": 2,
         "tackles_won": 9,
         "tackles_lost": 1,
        },
        
        {"name": "Fake Player #4", 
         "position": "Goalkeeper",
         "saves": 5,
         "goals_conceded": 1,
        },
        
        {"name": "Fake Player #5", 
         "position": "Goalkeper",
         "saves": 5,
         "goals_conceded": 1,
        },
        
        {"name": "Fake Player #6", 
         "position": "Defender",
         "goals": 0,
         "tackles_won": 3,
         "tackles_lost": 3,
        },
        
        {"name": "Fake Player #7", 
         "position": "Midfielder",
         "goals": True,
         "assists": False,
         "tackles_won": True,
         "tackles_lost": False,
        }
]

### Initialize the positions dictionary to store stats for each position
if __name__ == "__main__":
    positions = {}
    duplicates = set()
    for player in players:
        position = player["position"] 
        valid = initialize_positions(position, positions)
        if valid:
            add_player_stats(player, positions, duplicates)
    
    print("Hello! Welcome to the RPI Men's Club Soccer!")
    print("What would you like to see?")
    print("1. Display team stats\n2. Display player rating")
    while True:
        answer = input("Please select an option: ")
        if answer == "1":
            display_stats(positions)
        elif answer == "2":
            print("What player would you like to see?")
            player = int(input("Player: "))
            if player < len(players):
                print(f"{players[player]["name"]} rating: {calculate_player_rating(players[player]):.2f}")
            else:
                print("Player doesn't exist.")
        elif answer == "exit":
            print("Thank you!")
            break
        else:
            print("Not a valid choice!")
        