import requests
from bs4 import BeautifulSoup
import datetime
#from scrape1_squad_new1 import squads
from squad_data import squads


base_url = 'https://www.skysports.com'

# Input - squad stats from squad_new_1
# Pull squad stats for each team from squads, and calculate top scorer from column 3

tdstrip = squads()	

def apps_convert_dash():
   
    indexes = [0,1]
    newList = [[each_list[i] for i in indexes ] for each_list in tdstrip ]
    for eachlist in newList:
        if eachlist[1] == '-':
            eachlist[1] = '0'
    return(newList) 
#apps_convert_dash()

def apps_split():

    apps_col = apps_convert_dash()

    for eachlist in apps_col:
	# extract the split element list
        split_string = eachlist[1].split(' ')
    # delete the element from the eachlist object
        del eachlist[1]
    # append the splits to the original list
        for each_split in split_string:
            eachlist.append(each_split)
    return(apps_col)

#apps_split()    
       

def apps_convert_toint():
    converted = apps_split()
    
    for eachlist in converted:
        eachlist[1] = int(eachlist[1])
    return(converted)        


def get_max(lst, i, key_func=None):
    
    if not key_func: key_func = lambda x: x[i]
    res = max(lst, key=key_func)
    return [res[0], res[i]]

data = apps_convert_toint()

print("\n")
print("The player with most premier league appearances is: ")

result = (get_max(data,1, lambda x: int(x[1])))

print(result[0],",with a total appearances of:", result[1])
  
#(top_scorer, goals) = get_max(data,1, lambda x: int(x[1]))


if __name__ == '__main__':

    apps_convert_dash()
#   goals_convert_toint()
#    get_max()




