import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
base_url = 'https://www.hltv.org'

with open("stats.txt", "w") as f:
    f.write('match_id,team_name,player_name,K,hs,A,f,D,KAST,KD_diff,ADR,fk_dif,rating\n')

    pages = 100
    for page_idx in range(pages):
        print("Page: " + str(page_idx + 1))
        page = requests.get(base_url + '/results?offset=' + str(page_idx * 100), headers=headers)
        soup = BeautifulSoup(page.text, 'lxml')

        # Get a list of matches
        matches = [a.get('href') for a in soup.find_all('a', class_='a-reset') if a.get('href').find('matches') == 1]
        for match in matches:
            try:
                match_page = requests.get(base_url + match, headers=headers)

                # match_page = requests.get(base_url + matches[0], headers=headers)
                match_soup = BeautifulSoup(match_page.text, 'lxml')

                maps_raw = match_soup.find_all('div', class_='mapholder')

                maps_clean = [map.find('a').get('href') for map in maps_raw if map.find('a') is not None]

                for map_path in maps_clean:
                    detailed_page = requests.get(base_url + map_path, headers=headers)
                    detailed_soup = BeautifulSoup(detailed_page.text, 'lxml')
                    match_id = map_path.split('/')[-2]
                    match_info_rows = detailed_soup.find_all('div', class_='match-info-row')

                    stats_tables = detailed_soup.find_all('table', class_='stats-table')
                    for table in stats_tables:
                        team_name = table.find('th', class_='st-teamname').text

                        table_body = table.find('tbody')
                        rows = table_body.find_all('tr')
                        for row in rows:
                            player_name = row.find('td', class_='st-player').text

                            kills_hs = row.find('td', class_='st-kills').text.split(" ")
                            kills = kills_hs[0]
                            headshots = kills_hs[1].strip("(").strip(")")

                            assists_fl = row.find('td', class_='st-assists').text.split(" ")
                            assists = assists_fl[0]
                            if len(assists_fl) > 1:
                                flash_assists = assists_fl[1].strip("(").strip(")")
                            else:
                                flash_assists = "Null"

                            deaths = row.find('td', class_='st-deaths').text
                            kast = row.find('td', class_='st-kdratio').text.replace("%", "")
                            kd_diff = row.find('td', class_='st-kddiff').text
                            adr = row.find('td', class_='st-adr').text
                            fk_diff = row.find('td', class_='st-fkdiff').text
                            rating = row.find('td', class_='st-rating').text

                            f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(match_id, team_name,
                                                                                              player_name, kills,
                                                                                              headshots, assists,
                                                                                              flash_assists, deaths,
                                                                                              kast, kd_diff, adr,
                                                                                              fk_diff, rating))

            except:
                pass

print("Done")
