import requests
from bs4 import BeautifulSoup
import datetime

""" Input - pass in team to scrape """
""" Output - scrape the table for the teams league stats and print to text file """
""" That text file will contain the data to tweet """
""" If the team passed in doesnt match throw an error """

url = 'https://www.skysports.com/premier-league-table'


def scrape_table():
    team_name = input("Please enter team name: ")

    """ scrape table based on index[1] for team name passed in""" 
    team = None
    premier_r = requests.get(url)

    premier_soup = BeautifulSoup(premier_r.text, 'html.parser')

    premier_soup_tr = premier_soup.find_all('tr', {'class': 'standing-table__row'})
    result = [[r.text.strip() for r in td.find_all('td', {'class': 'standing-table__cell'})][:-1] for td in premier_soup_tr[1:]]

    for team_found in result:
        if team_found[1] == team_name:
            team = team_found
    table_results(team)            
           
def table_results(results):
    
    """ Print team stats to text file if found """
    """ The text file will be used to tweet """
    
    if results is not None:
        with open('premier_league_stats.txt', 'w') as file_open:
            file_open.write("{} are in position {} with a points total of {}".format (results[1], results[0], results[-1]))    
    else:
        raise RuntimeError("Unable to find team") 

       
if __name__ == '__main__':
    scrape_table()

