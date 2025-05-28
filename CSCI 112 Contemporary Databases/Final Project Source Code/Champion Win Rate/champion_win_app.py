import champion_win_function as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    client = MongoClient('172.31.60.76', 27017)
    
    print("""
    The Win Rate of champions in League of Legends is the amount of matches won divided by the amount of matches played.
    Though it should not be used alone, win rate can be used to visualize the metagame, or relative strength of champions.
    The metagame primarily changes through balance patches released by League of Legends developers, better known as nerfs and buffs.
    
    Here are the top 10 champions with the highest win rate across the entire dataset.
    """)
    
    
    total = fn.get_champion_win_rates(client, "CSCI_FINAL", 10)
    
    for Champion in total:
        pprint(Champion)
        
    print("""
    Now, here are the top 10 champions only for the year 2017.
    """)
        
    year_aggregate = fn.get_champion_win_rates_year(client, "CSCI_FINAL", 10, 2017)
    
    for Champion in year_aggregate:
        pprint(Champion)
    
    
    
    