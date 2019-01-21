import player_appearances
import player_sub_appearances
import player_yellowcards
import player_redcards
import player_topscorer
import squad_avg_age
import scrape_table_stats
import tweet_send

if __name__ == '__main__':

    player_appearances.apps_convert_dash()
    player_sub_appearances.apps_convert_dash()
    player_yellowcards.yellow_cards()
    player_redcards.red_cards()
    player_topscorer.goals_convert_dash()
    squad_avg_age.player_info()
    scrape_table_stats.scrape_table()
    tweet_send.make_tweet()
    

