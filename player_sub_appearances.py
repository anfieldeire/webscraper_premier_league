import requests
from bs4 import BeautifulSoup
import datetime
from operator import itemgetter
#from scrape1_squad_urls import table
from scrape1_squad_new1 import squads
#from squad_data import squads

""" Pull squad stats for each team from squads, split that column in 2 """
""" Take the 3rd value, set a zero if there is a dash, remove brackets, convert to int """
""" Get max on that value to get the max sub appearances across all players in all teams """

tdstrip = squads()


# For columns with no data insert two zeros one for apps + subapps

def apps_convert_dash():

# If there is a dash in that column convert into 2 zeros (one for starts, 2nd for sub apps)   
    indexes = [0,1]
    newList = [[each_list[i] for i in indexes ] for each_list in tdstrip ]
    for eachlist in newList:
        if eachlist[1] == '-':
            eachlist[1] = '0 0'
    return(newList) 


# Split the above column to 2 columns
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


def apps_bracket_remove():

    input = apps_split()

    apps_col1 =  [[i.replace(')', '').replace('(', '')for i in x] for x in input]
    return(apps_col1)
    

def apps_convert_toint():
    converted = apps_bracket_remove()
    
    for eachlist in converted:
        eachlist[2] = int(eachlist[2])
    return(converted)        


def get_max(lst, i, key_func=None):
    
    if not key_func: key_func = lambda x: x[i]
    res = max(lst, key=key_func)
    return [res[0], res[i]]

data = apps_convert_toint()
print("\n")
print("The player with most sub appearances is: ")

result = (get_max(data,2, lambda x: int(x[2])))

print(result[0],", with a sub appearances total of:", result[1])
  

if __name__ == '__main__':
    apps_convert_dash()



