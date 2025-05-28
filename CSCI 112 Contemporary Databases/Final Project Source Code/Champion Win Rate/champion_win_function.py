def get_champion_win_rates(client, database, limit):
    LOL = client[database].LeagueofLegends
    
    champion_win_rates = LOL.aggregate([
        {"$project": {
            "Champions" : { 
                "$concatArrays" : [
                    {"$objectToArray" : "$Top"},
                    {"$objectToArray" : "$Jungle"},
                    {"$objectToArray" : "$Middle"},
                    {"$objectToArray" : "$ADC"},
                    {"$objectToArray" : "$Support"}
                    ]
            },
            "rResult" : 1,
            "bResult" : 1
        }},
        {"$unwind": "$Champions"},
        {"$group": {
            "_id" : "$Champions.v",
            "wins_blue": {"$sum": {"$cond": [{"$and": [ {"$eq": ["$Champions.k","b"]},{"$eq": ["$bResult", 1]}]},1, 0] }},
            "wins_red": {"$sum": {"$cond": [{"$and":  [ {"$eq": ["$Champions.k","r"]}, {"$eq": ["$rResult", 1]}]},1, 0] }},
            "total_games_played": {"$sum":1}
        }},
        {"$addFields": {
            "win_rate": {"$round" : [ {"$multiply": [{"$divide": [{"$sum": ["$wins_blue", "$wins_red"]}, "$total_games_played"]}, 100]}, 2]}
        }},
        {"$sort" : {
            "win_rate" : -1
        }}, 
        {"$limit" : limit}])
        
    return champion_win_rates
    
def get_champion_win_rates_year(client, database, limit, year):
    LOL = client[database].LeagueofLegends

    champion_win_rates = LOL.aggregate([
        {"$match" : {"Year" : {"$eq" : year}}},
        {"$project": {
            "Champions" : { 
                "$concatArrays" : [
                    {"$objectToArray" : "$Top"},
                    {"$objectToArray" : "$Jungle"},
                    {"$objectToArray" : "$Middle"},
                    {"$objectToArray" : "$ADC"},
                    {"$objectToArray" : "$Support"}
                    ]
            },
            "rResult" : 1,
            "bResult" : 1
        }},
        {"$unwind": "$Champions"},
        {"$group": {
            "_id" : "$Champions.v",
            "wins_blue": {"$sum": {"$cond": [{"$and": [ {"$eq": ["$Champions.k","b"]},{"$eq": ["$bResult", 1]}]},1, 0] }},
            "wins_red": {"$sum": {"$cond": [{"$and":  [ {"$eq": ["$Champions.k","r"]}, {"$eq": ["$rResult", 1]}]},1, 0] }},
            "total_games_played": {"$sum":1}
        }},
        {"$addFields": {
            "win_rate": {"$round" : [ {"$multiply": [{"$divide": [{"$sum": ["$wins_blue", "$wins_red"]}, "$total_games_played"]}, 100]}, 2]}
        }},
        {"$sort" : {
            "win_rate" : -1
        }}, 
        {"$limit" : limit}
        ])
        
    return champion_win_rates