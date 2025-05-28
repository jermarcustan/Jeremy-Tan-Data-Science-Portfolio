def get_player_name(client, database, role):
    matchinfo = client[database].LeagueofLegends
    player_role = "$blue{0}".format(role)
    
    player_name_list = matchinfo.aggregate([
        {"$group":{"_id":player_role}},
        {"$project":{"_id":0, "Name":"$_id"}},
        {"$sort":{"Name":1}},
        ])
    return player_name_list

def get_fave_champ(client, database, role, player_name):
    lol = client[database].LeagueofLegends
    favorite = client[database].favorite
    
    favorite.drop()
    blue_player_role = "blue{0}".format(role)
    red_player_role = "red{0}".format(role)
    blue_champion = "${0}.b".format(role)
    red_champion = "${0}.r".format(role)
    
    
    #for blue{role}
    lol.aggregate([
    {"$match":{blue_player_role: player_name}},
    {"$project": {role:{"$objectToArray":"${}".format(role)}}},
    {"$unwind": "${}".format(role)},
    {"$group":{"_id": "${}.v".format(role) ,"times_picked":{"$sum": {"$cond": [{"$eq": ["${}.k".format(role),"b"]},1,0]}}}},
    {"$project":{"Player Name":player_name,"_id":0, "Champion":"$_id","times_picked":1}},
    {"$sort":{"times_picked":-1}},
    {"$merge":{"into":"favorite", "on":"_id"}}
    ])
   
    #for red{role}   
    lol.aggregate([
    {"$match":{red_player_role: player_name}},
    {"$project": {role:{"$objectToArray":"${}".format(role)}}},
    {"$unwind": "${}".format(role)},
    {"$group":{"_id": "${}.v".format(role) ,"times_picked":{"$sum": {"$cond": [{"$eq": ["${}.k".format(role),"r"]},1,0]}}}},
    {"$project":{"Player Name":player_name,"_id":0, "Champion":"$_id","times_picked":1}},
    {"$sort":{"times_picked":-1}},
    {"$merge":{"into":"favorite", "on":"_id"}}
    ])
    
    fave = favorite.aggregate([
    {"$group":{"_id":"$Champion","Total times picked":{"$sum":"$times_picked"}}},
    {"$project":{"Player Name": player_name,"_id":0, "Champion":"$_id","Total times picked":1}},
    {"$sort":{"Total times picked":-1}},
    {"$limit": 5}
    ])
    
    return fave