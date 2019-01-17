import requests
from bs4 import BeautifulSoup
import datetime


# Parse the Premier League Table and
# Return the Premier League Squad URLS - all urls returned in a single list

def table():
    url = 'https://www.skysports.com/premier-league-table'

    base_url = 'https://www.skysports.com'

    today = str(datetime.date.today())

    premier_r = requests.get(url)

#    print(premier_r.status_code)

    premier_soup = BeautifulSoup(premier_r.text, 'html.parser')

    premier_soup_tr = premier_soup.find_all('tr', {'class': 'standing-table__row'})

    full_team_urls = []
    
    premier_soup_tr = premier_soup.find_all('tr', {'class': 'standing-table__row'})
    result = [[r.text.strip() for r in td.find_all('td', {'class': 'standing-table__cell'})][:-1] for td in premier_soup_tr[1:]]
    teamurls = ([a.find("a", href=True)["href"] for a in premier_soup_tr[1:]])

    for item in teamurls:
        squad_name = (base_url + item + '-squad')
        full_team_urls.append(squad_name)

    return(full_team_urls)

if __name__ == '__main__':
    table()

