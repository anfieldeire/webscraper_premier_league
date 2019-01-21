
--- Prerequites

- pip3
- install requests
- import requests
- from bs4 import BeautifulSoup
- import datetime
- import string
- import sys
- from player_urls import player_urls
- from dateutil.relativedelta import relativedelta

--- Project Name: webscraper

--- Project Description: This is a webscraper to scrape the premier league table and produce various stats from the data
	- Stats printed to console:
		- Most appearances: player with most appearances this season, and the amount
		- Most sub appearances: player with most appearances this season, and the amount
		- Yellow cards: player with most red cards this season, and the amount
		- Red cards: player with most red cards this season, and the amount
		- Top Scorer: player with most goals scored this season, and the amount
		- Squad average ages: squads with the youngest & oldest average age in years
	- Tweet team info: select team to scrape from the league table, and tweet that out based on tweet configuration1
		

--- Installation:

	1. Install the prerequisites from pip
	2. Create your own credentials.py to link to tweet_send (see credentials_example)
	3. Run webscraper.py (Input a valid premier league team at the prompt)
	4. Check your twitter to ensure the tweet goes out from the program
