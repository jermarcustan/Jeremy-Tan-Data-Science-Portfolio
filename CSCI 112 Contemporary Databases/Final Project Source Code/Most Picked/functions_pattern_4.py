def get_champs_per_role(client, database, role):
    LOL = client[database].LeagueofLegends
    result = LOL.aggregate([
        { "$project": { role : {"$objectToArray" : "${0}".format(role)}}},
        { "$unwind": "${0}".format(role)}, 
        { "$group": {"_id": "${0}.v".format(role), "times_picked": {"$sum": 1}}},
        { "$addFields": {"pick_rate_percentage": { "$round" : [ {"$multiply": [{"$divide": ["$times_picked", 7620]}, 100]}, 2]}}},
        { "$project": {"_id": 0, "Champion": "$_id", "times_picked": 1, "pick_rate_percentage": 1}},
        { "$sort": {"times_picked": -1}}, 
        { "$limit": 10}
        ])
    return result
    
def get_champs_pick_rate(client, database, champ):
    LOL = client[database].LeagueofLegends
    champ_times_picked = LOL.aggregate([
        {"$match": {"$or": [{"Top.b": champ}, {"Jungle.b": champ}, {"Middle.b": champ}, {"ADC.b": champ}, {"Support.b": champ}, {"Top.r": champ}, {"Middle.r": champ}, {"Jungle.r": champ}, {"ADC.r": champ}, {"Support.r": champ}]}},
        {"$group": {"_id": champ, "times_picked" : {"$sum": 1}}},
        {"$project": {"_id": 0, "Champion": "$_id", "times_picked": 1, "pick_rate_percentage": { "$round" :[ {"$multiply": [{"$divide": ["$times_picked", 7620]}, 100]}, 2]}}}
        ])

    return champ_times_picked
    
def get_champs_per_role_2(client, database, role):
    LOL = client[database].LeagueofLegends
    LOL2 = client[database].totalpicked
    # reset the totalpicked collection
    LOL2.drop()
    column_name_blue = "$blue{0}Champ".format(role)
    column_name_red = "$red{0}Champ".format(role)
    final_column_name = "{0}_Champion".format(role)
    LOL.aggregate([
        {"$group": {"_id": column_name_blue, "times_picked" : {"$sum": 1}}},
        {"$project": {"_id": 0, "Champion": "$_id", "times_picked": 1}},
        {"$sort": {"times_picked": -1}},
        {"$merge": {"into": "totalpicked", "on": "_id"}}
        ])

    LOL.aggregate([
        {"$group": {"_id": column_name_red, "times_picked" : {"$sum": 1}}},
        {"$project": {"_id": 0, "Champion": "$_id", "times_picked": 1}},
        {"$sort": {"times_picked": -1}},
        {"$merge": {"into": "totalpicked", "on": "_id"}}
        ])


    total_times_picked = LOL2.aggregate([
        {"$group": {"_id": "$Champion", "total_times_picked": {"$sum": "$times_picked"}}},
        {"$project": {"_id": 0, final_column_name: "$_id", "count": "$total_times_picked", "pick_rate_percentage": { "$round" :[ {"$multiply": [{"$divide": ["$total_times_picked", 7620]}, 100]}, 2]}}}, 
        {"$sort": {"count": -1}},
        {"$limit": 10}
        ])

    return total_times_picked