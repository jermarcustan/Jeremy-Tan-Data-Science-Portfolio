import fave_champ_function as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == "__main__":
    client = MongoClient('172.31.80.59', 27017)
    
    print("Top, Jungle, Middle, ADC, Support")
    role = input("Please select role: ")
        
    prompt = input("Would you like to see the list of players? (Y/N) ")
    
    if prompt == "Y":
        top_player_list = fn.get_player_name(client, "final", role)
    
        for players in top_player_list:
            pprint(players)
        name = input("Please select player name: ")
        player_name = name
        
        fave_result = fn.get_fave_champ(client, "final", role , name)
    
        for fave in fave_result:
            pprint(fave)
    elif prompt =="N":
        
        name = input("Please type player name: ")
        player_name = name
        
        fave_result = fn.get_fave_champ(client, "final", role , name)
    
        for fave in fave_result:
            pprint(fave)
        
  
   
 
    
  
    
   