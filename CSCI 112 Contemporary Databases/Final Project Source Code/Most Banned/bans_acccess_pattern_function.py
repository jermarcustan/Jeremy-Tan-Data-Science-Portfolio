def get_most_banned(client, database, limit, order):
    """
    Get most banned
    param client MongoClient
    param database Database name
    """
    bans = client[database].bans_2
    
    most_banned = bans.aggregate([
    {"$project": {"Bans":{"$objectToArray":"$ban"}}},
    {"$unwind":"$Bans"},
    {"$match":{"Bans.v":{"$ne":""}}},
    {"$group":{"_id":"$Bans.v", "totalBans":{"$sum":1}}},
    {"$addFields": {"ban_rate_percentage": { "$round" : [ {"$multiply": [{"$divide": ["$totalBans", 7620]}, 100]}, 2]}}},
    {"$project":{"_id":0, "Champion":"$_id","totalBans":1, "ban_rate_percentage":1}},
    {"$sort":{"totalBans":order}},
    {"$limit":limit}
    ])
    
    return most_banned
    
def get_champion_ban_rate(client, database, champion_name):
    """
    Get most banned
    param client MongoClient
    param database Database name
    """
    bans = client[database].bans_2
    
    champion_ban_rate = bans.aggregate([
    {"$project": {"Bans":{"$objectToArray":"$ban"}}},
    {"$unwind":"$Bans"},
    {"$match":{"Bans.v":{"$ne":""}}},
    {"$group":{"_id":"$Bans.v", "totalBans":{"$sum":1}}},
    {"$addFields": {"ban_rate_percentage": { "$round" : [ {"$multiply": [{"$divide": ["$totalBans", 7620]}, 100]}, 2]}}},
    {"$project":{"_id":0, "Champion":"$_id","totalBans":1, "ban_rate_percentage":1}},
    {"$match":{"Champion":champion_name}},
    {"$sort":{"totalBans":-1}}
    ])
    
    return champion_ban_rate