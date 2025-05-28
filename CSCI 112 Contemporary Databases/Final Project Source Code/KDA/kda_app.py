import kda_function as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    client = MongoClient('172.31.60.76', 27017)
    
    print("""
    K/D/A is a common metric used for judging player performance in League of Legends.
    It is calculated by the formula (Kills + Assists) / Deaths.
    Here are the top 10 players with the highest and lowest KDA in League of Legends esports.
    """)
    total = fn.get_player_kill_statistics(client, "CSCI_FINAL", "kdaValue", -1, 10)
    
    for Player in total:
        pprint(Player)
        
    print("")
        
    lowest = fn.get_player_kill_statistics(client, "CSCI_FINAL", "kdaValue", 1, 10)
    
    for Player in lowest:
        pprint(Player)
        
    print("""
    What about the most bloodthirsty players, with the most kills?
    """)
    
    kill_aggregate = fn.get_player_kill_statistics(client, "CSCI_FINAL", "totalKills", -1, 10)
    
    for Player in kill_aggregate:
        pprint(Player)
        
    print("""
    And, lastly, what about the best supporting roles, with the most assists?
    """)
        
    assist_aggrregate = fn.get_player_kill_statistics(client, "CSCI_FINAL", "totalAssists", -1, 10)
    
    for Player in assist_aggrregate:
        pprint(Player)
    
    
    
    
    