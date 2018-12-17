import pandas as pd

stats_path = '../data/matches_clean.csv'
stats_cols = ['match_id', 'team_name', 'kills', 'headshots', 'assists', 'flash_assists', 'deaths',
              'kd_ratio', 'kd_diff', 'adr', 'fk_dif', 'rating']
stats_df = pd.read_csv(stats_path, names=stats_cols, skiprows=1, index_col=False, skipinitialspace=True)

tiers_path = '../data/team_tiers.csv'
tiers_cols = ['team', 'tier']
tiers_df = pd.read_csv(tiers_path, names=tiers_cols, skiprows=1, index_col=False, skipinitialspace=True)

# stats_df = stats_df[:5] #For testing purposes

team_names = stats_df.team_name.unique()
for team in team_names:
    row = tiers_df.loc[tiers_df['team'] == team]
    print(team)
    tier = row['tier'].values[0]
    stats_df.loc[stats_df.team_name == team, 'tier'] = tier

stats_df.to_csv('../data/final_joined.csv', index=False)