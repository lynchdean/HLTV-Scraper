import pandas as pd

stats_columns = ['match_id', 'team_name', 'kills', 'headshots', 'assists', 'flash_assists', 'deaths',
              'kd_ratio', 'kd_diff', 'adr', 'fk_dif', 'rating']

tiers_columns = ['team', 'tier']

stats_path = '../data/match_avgs_clean.csv'
tiers_path = '../data/team_tiers.csv'

stats_df = pd.read_csv(stats_path, names=stats_columns, skiprows=1, index_col=False, skipinitialspace=True)
tiers_df = pd.read_csv(tiers_path, names=tiers_columns, skiprows=1, index_col=False, skipinitialspace=True)

# stats_df = stats_df[:5]

stats_df['tiers'] = "missing"

# for index, row in stats_df.iterrows():
match_ids = stats_df.match_id.unique()


for match in match_ids:
    tier_row = tiers_df.loc[tiers_df['team'] == match]

    print(tier_row)

    tier = tier_row.iloc[0]['tier']

    # stats_df.loc[stats_df.team_name == team_name, 'tiers'] = tier
    #
    # print(index, team_name)

stats_df.to_csv('../data/final_joined.csv', index=False)