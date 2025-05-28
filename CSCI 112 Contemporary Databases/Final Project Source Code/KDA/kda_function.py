def get_player_kill_statistics(client, database, sort, order, limit):
    LOLKills = client[database].Kills
    
    kill_statistics = LOLKills.aggregate([
        {"$project": {
            "Participants" : {
                "$objectToArray" : "$Participants"
            }
        }},
        {"$unwind": "$Participants"},
        {"$match":{"Participants.v":{"$nin":["", "None"]}}},
        {"$group": {
            "_id" : "$Participants.v",
            "totalKills" : { "$sum" : { "$cond" : [{ "$eq" : ["$Participants.k", "Killer"]}, 1, 0]}},
            "totalDeaths" : { "$sum" : {"$cond" : [{"$eq" : ["$Participants.k", "Victim"]}, 1, 0]}},
            "totalAssists" : { "$sum" : {"$cond" : [{"$in" : ["$Participants.k", ["Assist_1", "Assist_2", "Assist_3", "Assist_4"]]}, 1, 0]}}
        }},
        {"$addFields": {
            "kdaValue": { "$cond" : [
                { "$eq" : [ "$totalDeaths", 0]},
                "None",
                { "$round" : [ {"$divide": [{"$sum": ["$totalKills", "$totalAssists"]}, "$totalDeaths"]}, 2]}
                ]
        }}},
        {"$sort" : { sort : order, "totalKills" : -1}},
        {"$limit" : limit}
        ])
        
    return kill_statistics
    