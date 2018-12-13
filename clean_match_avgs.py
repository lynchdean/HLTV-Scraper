import pandas as pd

# dataset headers
df_columns = ['match_id', 'team_name', 'player_name', 'kills', 'headshots', 'assists', 'flash_assists', 'deaths',
              'kd_ratio', 'kd_diff', 'adr', 'fk_dif', 'rating']

csv_path = 'match_avgs.csv'
df = pd.read_csv(csv_path, names=df_columns, skiprows=1, index_col=False, skipinitialspace=True)

team_name_vc = df['team_name'].value_counts()

game_threshold = 5 # Teams must have played at least this many games
under_game_treshold = []
for team_name, games_played in team_name_vc.items():
    if games_played < game_threshold:
        under_game_treshold.append(team_name)

for team_name in under_game_treshold:
    df = df[df.team_name != team_name]

df.to_csv('match_avgs_clean.csv', index=False)
print("Done.")