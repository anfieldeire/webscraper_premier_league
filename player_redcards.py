import requests
from bs4 import BeautifulSoup
import datetime
from operator import itemgetter
#from scrape1_squad_new1 import squads
from squad_data import squads

# Objective:  Pull squad stats for each team from squads, and most red cards from column 5

# Input: Squad stats is in a list for each player, with the entire thing in a list
# Output: the players name and yellow cards total using get_max


def red_cards():

# Return just 2 columns from player_stats, using indexes   
# Zero for name, 4 for the red cards column
# Convert any dashes in column 4 to zeros 

    player_stats = squads()

    indexes = [0,4]
    newList = [[each_list[i] for i in indexes ] for each_list in player_stats ]
    
    for eachlist in newList:
        if eachlist[1] == '-':
            eachlist[1] = 0
    return(newList) 

def red_cards_convert_toint():
    converted = red_cards()
    
    for eachlist in converted:
#        print("Second func from redcards")
        eachlist[1] = int(eachlist[1])

    return(converted)        

def get_max(lst, i, key_func=None):
          
    if not key_func: key_func = lambda x: x[i]
    res = max(lst, key=key_func)
    return [res[0], res[i]]

data = red_cards_convert_toint()

print("The player with the most red cards is:")
result = (get_max(data,1, lambda x: int(x[1])))
print("{} with {} red cards".format(result[0],result[1]))


if __name__ == '__main__':
    red_cards()




