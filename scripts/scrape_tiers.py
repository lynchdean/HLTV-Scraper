import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
base_url = 'https://www.hltv.org'

# dataset headers
df_columns = ['match_id', 'team_name', 'player_name', 'kills', 'headshots', 'assists', 'flash_assists', 'deaths',
              'kd_ratio', 'kd_diff', 'adr', 'fk_dif', 'rating']

csv_path = '../data/match_avgs_clean.csv'
df = pd.read_csv(csv_path, names=df_columns, skiprows=1, index_col=False, skipinitialspace=True)
unique_teams = df.team_name.unique()

with open("../data/ranks.csv", "w") as f:
    f.write('team,rank\n')

    counter = 0
    total = len(unique_teams)
    for team_name in unique_teams:
        query = team_name.replace(" ", "+")
        page = requests.get(base_url + '/search?query=' + query, headers=headers)
        soup = BeautifulSoup(page.text, 'lxml')


        team_links = soup.findAll("a", href=re.compile("/team/[0-9]+/"))
        for link in team_links:
            if team_name == link.text:
                team_page = requests.get(base_url + link['href'], headers=headers)
                team_soup = BeautifulSoup(team_page.text, 'lxml')
                profile = team_soup.find('div', class_='profile-team-stat')
                rank = profile.find('span', class_='right').text.replace("#", "")

                if rank == "-":
                    tier = "T6"
                elif int(rank) in range(0, 11):
                    tier = "T1"
                elif int(rank) in range(11, 21):
                    tier = "T2"
                elif int(rank) in range(21, 31):
                    tier = "T3"
                elif int(rank) in range(31, 101):
                    tier = "T4"
                elif int(rank) in range(101, 301):
                    tier = "T5"
                else:
                    tier = "T6"

                counter += 1
                print("[{}/{}] {},{}".format(counter, total, team_name, tier))
                f.write("{},{}\n".format(team_name, tier))
                break

print("\nDone.")