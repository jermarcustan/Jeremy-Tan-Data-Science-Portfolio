def get_average_game_length_list(client, database, limit):
    LOL = client[database].LeagueOfLegendsTeams
    

    average_game_length_list = LOL.aggregate([
        {"$group": {"_id": {"League": "$League","Year": "$Year"}, "average_game_length": {"$avg":"$gamelength"}}},
        {"$addFields": { "Average_game_length" : {"$round": ["$average_game_length", 2]}}},
        {"$project": {"_id": 0, "id": "$_id", "Average_game_length": 1}},
        {"$sort": {"id.Year": 1}},
        {"$limit": limit}
        ])
    
    return average_game_length_list
    
    
def get_average_game_length_specific(client, database, league_name, year):
    LOL = client[database].LeagueOfLegendsTeams
    

    average_game_length_specific = LOL.aggregate([
        {"$match":{"League": league_name, "Year": year}},
        {"$group": {"_id": {"League": "$League","Year": "$Year"}, "average_game_length": {"$avg":"$gamelength"}}},
        {"$addFields": { "Average_game_length" : {"$round": ["$average_game_length", 2]}}},
        {"$project": {"_id": 0, "id": "$_id", "Average_game_length": 1}},
        {"$sort": {"id.Year": 1}}
        ])
    
    return average_game_length_specific