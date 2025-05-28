import functions_pattern_3 as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    client = MongoClient('172.31.65.1', 27017)
    botduos = fn.get_bot_duo(client, "CSCI_FINAL")
    print("The Top 10 highest win rate bot duos")
    for duo in botduos:
        pprint(duo)