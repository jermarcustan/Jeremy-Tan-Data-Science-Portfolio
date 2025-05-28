import functions_pattern_4 as fn
from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    client = MongoClient('172.31.65.1', 27017)
    print("Finding the pick rate of champions in League of Legends ")
    print("Options:")
    print("1 - Get the top 10 most picked champs per role")
    print("2 - Get the pick rate of a particular champ")
    print("3 - Exit")
    while True:
        option = raw_input("Enter Option: ")
        if option == "1":
            role = raw_input("Enter Role: ")
            print("The top 10 most picked {0} champs").format(role)
            total = fn.get_champs_per_role(client, "CSCI_FINAL", role)
            for champ in total:
                pprint(champ)
        if option == "2":
            champ = raw_input("Enter the Champion Name: ")
            per_champ = fn.get_champs_pick_rate(client, "CSCI_FINAL", champ)
            for champ in per_champ:
                pprint(champ)
        if option == "3":
            break