import requests
from bs4 import BeautifulSoup
import datetime
from scrape1_squad_urls import table


""" Input: full squad urls in one list """
""" Output: Get squad stats for each player (in a list) in each squad, and output in one list """

team_table = table()

def squads():
        
    iter = 0
    while iter < 1:
        player_stats = []
        x = []
        for i in team_table:

                squad_r = requests.get(i)

                now = datetime.datetime.now()
                premier_squad_soup = BeautifulSoup(squad_r.text, 'html.parser')
                premier_squad_table = premier_squad_soup.find_all('table', {'class': 'table -small no-wrap football-squad-table '})
                headings = []
                playerurls = []
                full_links = []
                find_team_name = premier_squad_soup.find('span',{'class': 'swap-text__target'})
                for table in premier_squad_table:

                    table_head = table.find('thead')
                    head_rows = table_head.find_all('tr')

                    for item in head_rows:
                        headers = item.find_all('th')

                    table_body = table.find('tbody')
                    rows = table_body.find_all('tr')
                    for row in rows:
                        td = row.find_all('td')
                        x = [x.text.strip() for x in td]
                        position_teamname = (headers[0].text,find_team_name.text)
                        x[2]
                        x.extend(position_teamname)
                        player_stats.append(x)
        iter = iter + 1
    return(player_stats)

if __name__ == '__main__':
    squads()


