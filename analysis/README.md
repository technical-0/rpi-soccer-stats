This script's purpose is to calculate the total statistics for each position and calculate a player's match rating.
Total statistics:
Statistics for every outfield position are the same, and the goalkeepers get their own stat sheet.
It takes in every valid stat from each player input, but rejects the player if all statistics are invalid or the position is invalid.
Player match rating*:
The stats available for the player is taken into consideration when applying it into a set formula for each position, from 0-10
Goalkeeper - score = rating + (saves * 0.15) - (goals_conceded * 0.4)
Defender - score = rating + goals + (assists * 0.6) + (tackles_won * 0.05) - (tackles_lost * 0.05)
Midfielder - score = rating + (goals * 0.8) + (assists * 0.5) + (tackles_won * 0.08) - (tackles_lost * 0.04)
Forward - score = rating + (goals * 0.6) + (assists * 0.4) + (tackles_won * 0.1) - (tackles_lost * 0.05)
Current limitations are: real stats from games aren't available yet, so these stats are all tests
*Formulas aren't fully reliable yet, so they will get changed in the future.
