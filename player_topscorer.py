import requests
from bs4 import BeautifulSoup
import datetime
from scrape1_squad_new1 import squads
#from squad_data import squads

# Objective:  Pull squad stats for each team from squads, and calculate top scorer from column 3

# Input: Squad stats is in a list for each player, with the entire thing in a list
# Output: the players name and goals total using get_max

player_stats = squads()	


def goals_convert_dash():
# If there is a dash in the column convert that to a zero 0

    indexes = [0,2]
    newList = [[each_list[i] for i in indexes ] for each_list in player_stats ]
    for eachlist in newList:
        if eachlist[1] == '-':
            eachlist[1] = 0
    return(newList) 


def goals_convert_toint():
# Convert the column used for get_max to an integer    

    converted = goals_convert_dash()
    
    for eachlist in converted:
        eachlist[1] = int(eachlist[1])
    return(converted)        

def get_max(lst, i, key_func=None):
    
    if not key_func: key_func = lambda x: x[i]
    res = max(lst, key=key_func)
    return [res[0], res[i]]

data = goals_convert_toint()

print("Premier league top goal scorer is: ")

result = (get_max(data,1, lambda x: int(x[1])))

print(result[0], "with a goals total of", result[1])
  

if __name__ == '__main__':
    goals_convert_dash()




