import requests
from bs4 import BeautifulSoup
import datetime
import time
import string
import sys
import re
from player_urls import player_urls
from dateutil.relativedelta import relativedelta

""" Input - player urls """
""" This takes player urls for each team and calculates the age of each player """
""" For each team the average age is calculated """
""" The output is the oldest team and youngest team by average age """

player_urls = player_urls()

def player_info():
    """ Scrape player info for each player for each team  """   
    """ Name, DOB, Club, squad number etc """
    all_teams = []
    for x in player_urls:
        teams = []
        for i in x:
            squad_r = requests.get(i)
            now = datetime.datetime.now()
            player_soup = BeautifulSoup(squad_r.text, 'html.parser')
            premier_soup1 = player_soup.find('div', {'class': 'row-table details -bp30'})

            # Exact match for class name
            divs = player_soup.select( 'div[class="col"]')

            team = []
            pnew = []          
            club = player_soup.find("span", itemprop="affiliation")

            for div in divs:
                ps = div.find_all('p')
                pnew = [p.text.split(":")[1] for p in ps]
                pnew.append(club.text)
                for item in pnew:                   
                    team.append(item)
            teams.append(team)
        all_teams.append(teams)   
#    return(all_teams)
    player_dates(all_teams)


def player_dates(players):
    """ Convert the column with a string date in it to a python date object """
    """ If there is no date just default to age 21, these are usually u21 players """
    all_teams1 = []
#    players = player_info()
   
    today = datetime.date.today()
    for y in players:
        teams = []
        for x in y:
            # if no slash then there is no DOB in x[1]
            if '/' in x[1]:
                yr = datetime.datetime.strptime(x[1], '%d/%m/%Y').date()
                age = (today - yr)
                years = (age.days / 365.25)
                x.append(years)
                teams.append(x)
            else:
                x.append(float(21))
                teams.append(x)
        all_teams1.append(teams)            
#    return(all_teams1)
    average_age(all_teams1)

#player_dates()

def average_age(players):
    """ Find the average each in each team """
#    players = player_dates()    
    all_teams = []
    for x in players:
        team = []
        for i in x:
            team_total_age = sum(float(i[-1]) for i in x)
            player_count = len(x)
        team_avg_age = team_total_age / player_count        
        team.append(i[-2])
        team.append(team_avg_age)
        all_teams.append(team)
#    return(all_teams)
    teams_min_max_age(all_teams)   

def my_max_by_weight(sequence):
    """Compare elements by their weight stored in the 2nd element """
    
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        
        if item[1] > maximum[1]:
            maximum = item
    return maximum


def my_min_by_weight(sequence):
    """ Compare elements by their weight stored in their 2nd element """
   
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:
        # Compare elements by their weight stored
        # in their second element.
        if item[1] < maximum[1]:
            minimum = item
    return minimum

def teams_min_max_age(team_ages):
    """ Find the teams with the youngest & oldest avg age """
#    team_ages = average_age()
    
    my_max = my_max_by_weight(team_ages)

    my_min = my_min_by_weight(team_ages)
    print("\n")
    print("The oldest team is {} with an average age of {} years".format(my_max[0], my_max[1]))
    print("The youngest team is {} with an average age of {} years".format(my_min[0], my_min[1]))

if __name__ == '__main__':
    player_info()

        


           
        
    
    
