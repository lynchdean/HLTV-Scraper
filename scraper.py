import time

import requests
from bs4 import BeautifulSoup

# Get a list of matches
base_url = 'https://www.hltv.org'
page = requests.get(base_url + '/results')
soup = BeautifulSoup(page.text, 'lxml')

#Get a list of matches
matches = [a.get('href') for a in soup.find_all('a', class_='a-reset') if a.get('href').find('matches') == 1]

#Get detailed stats page
match_page = requests.get(base_url + matches[0])
match_soup = BeautifulSoup(match_page.text, 'lxml')

with open("stats.txt", "w") as f:
    f.write('match_id, team_name, player_name, kills, assists, flash_assists, deaths, kd_ratio, kd_diff, adr, fk_dif, rating\n')

i = 0
while i < len(matches):
    match_page = requests.get(base_url + matches[i])
    match_soup = BeautifulSoup(match_page.text, 'lxml')

    maps_raw = match_soup.find_all('div', class_='mapholder')
    for map in maps_raw:
        map_path = map.find('a').get('href')
        match_id = map_path.split('/')[-2]
        detailed_page = requests.get(base_url + map_path)
        detailed_soup = BeautifulSoup(detailed_page.text, 'lxml')

        stats_tables = detailed_soup.find_all('table', class_='stats-table')
        for table in stats_tables:
            team_name = table.find('th', class_='st-teamname').text

            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                player_name = row.find('td', class_='st-player').text

                kills_hs = (row.find('td', class_='st-kills').text).split(" ")
                kills = kills_hs[0]

                headshots = kills_hs[1].strip("(").strip(")")

                assists_fl = row.find('td', class_='st-assists').text.split(" ")
                assists = assists_fl[0]
                flash_assists = assists_fl[1].strip("(").strip(")")

                deaths = row.find('td', class_='st-deaths').text
                kd_ratio = float(row.find('td', class_='st-kdratio').text.strip("%")) / 100
                kd_diff = row.find('td', class_='st-kddiff').text.strip("+")
                adr = row.find('td', class_='st-adr').text
                fk_dif = row.find('td', class_='st-kddiff').text.strip("+")
                rating = row.find('td', class_='st-rating').text
                with open("stats.txt", "a") as f:
                    f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(match_id, team_name, player_name, kills, assists, flash_assists, deaths, kd_ratio, kd_diff, adr, fk_dif, rating))
                # print(match_id, team_name, player_name, kills, assists, flash_assists, deaths, kd_ratio, kd_diff, adr, fk_dif, rating)
    i += 1



            deaths = row.find('td', class_='st-deaths').text
            kd_ratio = float(row.find('td', class_='st-kdratio').text.strip("%")) / 100
            kd_diff = row.find('td', class_='st-kddiff').text.strip("+")
            adr = row.find('td', class_='st-adr').text
            fk_dif = row.find('td', class_='st-kddiff').text.strip("+")
            rating = row.find('td', class_='st-rating').text

            print(match_id, team_name, player_name, kills, assists, flash_assists, deaths, kd_ratio, kd_diff, adr, fk_dif, rating)
