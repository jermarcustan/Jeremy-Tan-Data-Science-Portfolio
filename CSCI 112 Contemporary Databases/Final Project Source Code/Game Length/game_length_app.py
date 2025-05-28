import game_length_functions as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    client = MongoClient('172.31.31.7', 27017)
   
    list_or_Team = raw_input("Would you like to see the Average game length list, or a specific League and Year (L for List and LY for League and Year): " )
    
    if list_or_Team ==  "L" :
        
        count = int(raw_input("How many Teams would you like to see in the list (Max:44): "))
    
        list_total = fn.get_average_game_length_list(client, "CSCI_FINAL", count)
    
        for game_length in list_total:
            pprint(game_length)
            
    elif list_or_Team ==  "LY" :
    
        league_name = raw_input("What league would you like to see: ")
        
        year = int(raw_input("And what year would you like to see: "))
    
        list_total = fn.get_average_game_length_specific(client, "CSCI_FINAL", league_name, year)
    
        for game_length in list_total:
            pprint(game_length)
