def get_team_win_list(client, database, limit):
    LOL = client[database].LeagueOfLegendsTeams

    Team_win_list = LOL.aggregate([
        {"$project": {
            "Team" : {
                "$objectToArray" : "$Team"
            },
            "rResult": 1,
            "bResult": 1
        }},
        {"$unwind": "$Team"},
        {"$group": {
            "_id" : "$Team.v",
            "wins_blue": {"$sum": {"$cond": [{"$and": [ {"$eq": ["$Team.k","b"]},{"$eq": ["$bResult", 1]}]},1, 0] }},
            "wins_red": {"$sum": {"$cond": [{"$and":  [ {"$eq": ["$Team.k","r"]}, {"$eq": ["$rResult", 1]}]},1, 0]}},
            "total_games_played": {"$sum":1}
            }
            },
            {"$addFields": {
                 "win_rate": {"$round" : [ {"$multiply": [{"$divide": [{"$sum": ["$wins_blue", "$wins_red"]}, "$total_games_played"]}, 100]}, 2]}
            }},
            {"$sort": {"total_games_played": -1}},
            {"$limit": limit}
    ])
    
    return Team_win_list

def get_team_wins(client, database, team_name):
    LOL = client[database].LeagueOfLegendsTeams

    Team_wins = LOL.aggregate([
        {"$project": {
            "Team" : {
                "$objectToArray" : "$Team"
            },
            "rResult": 1,
            "bResult": 1
        }},
        {"$unwind": "$Team"},
        {"$group": {
            "_id" : "$Team.v",
            "wins_blue": {"$sum": {"$cond": [{"$and": [ {"$eq": ["$Team.k","b"]},{"$eq": ["$bResult", 1]}]},1, 0] }},
            "wins_red": {"$sum": {"$cond": [{"$and":  [ {"$eq": ["$Team.k","r"]}, {"$eq": ["$rResult", 1]}]},1, 0]}},
            "total_games_played": {"$sum":1}
            }
            },
            {"$addFields": {
                 "win_rate": {"$round" : [ {"$multiply": [{"$divide": [{"$sum": ["$wins_blue", "$wins_red"]}, "$total_games_played"]}, 100]}, 2]}
            }},
            {"$match":{"_id": team_name}}
    ])
    
    return Team_wins
    