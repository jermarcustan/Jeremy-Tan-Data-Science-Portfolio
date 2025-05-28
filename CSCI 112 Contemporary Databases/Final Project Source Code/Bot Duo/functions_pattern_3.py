def get_bot_duo(client, database):
    LOL = client[database].LeagueofLegends
    results = LOL.aggregate([
        {"$project": {"ChampDuos": [{"k": "blueDuo", "v": ["$ADC.b", "$Support.b"]}, {"k": "redDuo", "v": ["$ADC.r", "$Support.r"]}], "rResult": 1, "bResult": 1}},
        { "$unwind": "$ChampDuos"},
        { "$group": {
            "_id" : "$ChampDuos.v",
            "wins_blue": {"$sum": {"$cond": [{"$and": [ {"$eq": ["$ChampDuos.k","blueDuo"]},{"$eq": ["$bResult", 1]}]},1, 0] }},
            "wins_red": {"$sum": {"$cond": [{"$and":  [ {"$eq": ["$ChampDuos.k","redDuo"]}, {"$eq": ["$rResult", 1]}]},1, 0]}},
            "total_games_played": {"$sum":1}
            }
            },
        { "$addFields": {
                 "win_rate": {"$round" : [ {"$multiply": [{"$divide": [{"$sum": ["$wins_blue", "$wins_red"]}, "$total_games_played"]}, 100]}, 2]}
            }},
        { "$project": {"_id": 0, "ChampDuo": "$_id", "wins_blue": 1, "wins_red": 1, "total_games_played": 1, "win_rate": 1}},
        {"$sort": {"total_games_played": -1}},
        {"$limit": 10}
        ])
    return results
    
def get_bot_duo_2(client, database):
    LOL = client[database].LeagueofLegends
    LOL2 = client[database].total_blue
    LOL3 = client[database].total_red
    LOL4 = client[database].total
    # reset the totalpicked collection
    LOL2.drop()
    LOL3.drop()
    LOL4.drop()

    LOL.aggregate([
        {"$match": {"bResult" : 1}},
        {"$group": {"_id": ["$blueADCChamp", "$blueSupportChamp"], "times_won_blue" : {"$sum": 1}}},
        {"$project": {"_id": 0, "Bot_Duo_Blue": "$_id", "times_won_blue": 1}},
        {"$sort": {"times_won_blue": -1}},
        {"$merge": {"into": "total_blue", "on": "_id"}}
        ])

    LOL.aggregate([
        {"$match": {"bResult" : 0}},
        {"$group": {"_id": ["$blueADCChamp", "$blueSupportChamp"], "times_lost_blue" : {"$sum": 1}}},
        {"$project": {"_id": 0, "Bot_Duo_Blue": "$_id", "times_lost_blue": 1}},
        {"$sort": {"times_lost_blue": -1}},
        {"$merge": {"into": "total_blue", "on": "_id"}}
        ])

    LOL.aggregate([
        {"$match": {"rResult" : 1}},
        {"$group": {"_id": ["$redADCChamp", "$redSupportChamp"], "times_won_red" : {"$sum": 1}}},
        {"$project": {"_id": 0, "Bot_Duo_Red": "$_id", "times_won_red": 1}},
        {"$sort": {"times_won_red": -1}},
        {"$merge": {"into": "total_red", "on": "_id"}}
        ])

    LOL.aggregate([
        {"$match": {"rResult" : 0}},
        {"$group": {"_id": ["$redADCChamp", "$redSupportChamp"], "times_lost_red" : {"$sum": 1}}},
        {"$project": {"_id": 0, "Bot_Duo_Red": "$_id", "times_lost_red": 1}},
        {"$sort": {"times_lost_red": -1}},
        {"$merge": {"into": "total_red", "on": "_id"}}
        ])

    LOL2.aggregate([
        {"$group": {"_id": "$Bot_Duo_Blue", "times_won": {"$sum": "$times_won_blue"}, "times_lost_blue": {"$sum": "$times_lost_blue"}}},
        {"$project": {"_id": 0, "Bot_Duo": "$_id", "times_won": 1, "total_games": {"$sum" : ["$times_won", "$times_lost_blue"]}}},
        {"$merge": {"into": "total", "on": "_id"}}
        ])

    LOL3.aggregate([
        {"$group": {"_id": "$Bot_Duo_Red", "times_won": {"$sum": "$times_won_red"}, "times_lost_red": {"$sum": "$times_lost_red"}}},
        {"$project": {"_id": 0, "Bot_Duo": "$_id", "times_won": 1, "total_games": {"$sum" : ["$times_won", "$times_lost_red"]}}},
        {"$merge": {"into": "total", "on": "_id"}}
        ])

    bot_duo = LOL4.aggregate([
        {"$match": {"total_games": {"$ne" : 0}}},
        {"$group": {"_id": "$Bot_Duo", "total_wins": {"$sum": "$times_won"}, "total_games_of_duo": {"$sum": "$total_games"}}},
        {"$project": {"_id": 0, "Bot_Duo": "$_id", "total_wins": 1, "total_games_of_duo": 1, "win_rate": {"$round" : [ {"$multiply": [{"$divide": ["$total_wins", "$total_games_of_duo"]}, 100]}, 2]}}},
        {"$sort": {"total_wins": -1}},
        {"$limit": 10}
        ])
    

    return bot_duo