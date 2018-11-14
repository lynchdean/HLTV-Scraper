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

maps_raw = match_soup.find_all('div', class_='mapholder') #.find('a').get('href')
for map in maps_raw:
    map_path = map.find('a').get('href')
    detailed_page = requests.get(base_url + map_path)
    detailed_soup = BeautifulSoup(detailed_page.text, 'lxml')

    stats_tables = detailed_soup.find_all('table', class_='stats-table')
    print(stats_tables)

# detailed_page = requests.get(base_url + detailed_path)
# detailed_path = match_soup.find('div', class_='stats-detailed-stats').find('a').get('href')
# time.sleep(1)
# detailed_soup = BeautifulSoup(detailed_page.text, 'lxml')
# print(detailed_soup)
#
# test = detailed_soup.find('div', class_='headline')
# print(test)