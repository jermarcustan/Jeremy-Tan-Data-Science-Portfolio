import Team_wins_functions as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == "__main__":
    client = MongoClient('172.31.31.7', 27017)
    
    list_or_Team = raw_input("Would you like to see the team win List or the wins of a specific team (L for List and T for Team): " )
    
    if list_or_Team ==  "L" :
        
        count = int(raw_input("How many Teams would you like to see in the list: "))
    
        list_total = fn.get_team_win_list(client, "CSCI_FINAL", count)
    
        for TeamTag in list_total:
            pprint(TeamTag)
            
    elif list_or_Team ==  "T" :
    
        team_name = raw_input("Which Team would you like to see: ")
    
        team_wins = fn.get_team_wins(client, "CSCI_FINAL", team_name)
    
        for TeamTag in team_wins:
            pprint(TeamTag)