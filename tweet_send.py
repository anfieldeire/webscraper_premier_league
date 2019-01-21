import tweepy
from time import sleep
from credentials import *
from scrape_table_stats import table_results

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def make_tweet():
#    team_name = 'Tottenham Hotspur'
    
#    stats = table_results(team_name)

    my_file=open('premier_league_stats.txt','r')
    file_lines=my_file.readlines()
    my_file.close()
    

    # Create a for loop to iterate over file_lines
    for line in file_lines:
        try:
            if line != '\n':
                print(line)
                api.update_status(line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)

if __name__ == '__main__':
    make_tweet()
