import bans_acccess_pattern_function as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == "__main__":
    client = MongoClient('172.31.80.59', 27017)
    
    list_or_champ = input("Would you like to see the Ban List or a specific Champion's Ban Rate (L for List and C for Champion):  ")
    
    
    if list_or_champ == "L":
        
        count = int(input("How many Champions would you like to see in the most banned list: "))
        orders = int(input("Would you like to see the most or least banned  (1 for Least Banned and -1 for the Most Banned) : "))
        
        bans_result = fn.get_most_banned(client, "final", count, orders)
    
        for ban in bans_result:
            pprint(ban)
        
            
    elif list_or_champ == "C":
    
        champ_name = input("Which Champion's ban rate would you like to see: ")
        champ_ban_rate = fn.get_champion_ban_rate(client, "final", champ_name)
    
        for champ in champ_ban_rate:
            pprint(champ)
    
    