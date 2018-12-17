import pandas as pd

# pd.set_option('display.max_row', 1000)
# pd.set_option('display.max_columns', 50)

df_columns = ['match_id', 'team_name', 'kills', 'headshots', 'assists', 'flash_assists', 'deaths',
              'kd_ratio', 'kd_diff', 'adr', 'fk_dif', 'rating']

csv_path = '../data/130k_manual_cln.csv'
# csv_path = '../data/test.csv'

df = pd.read_csv(csv_path, names=df_columns, skiprows=1, index_col=False, skipinitialspace=True)
df.drop_duplicates()

match_ids = df.match_id.unique()

with open('../data/match_avgs.csv', 'w') as csv:
    for match_id in match_ids:
        match_df = df.loc[df['match_id'] == match_id]

        if len(match_df.index) == 10:  # Only add the match if it has the full 10 players.
            team_names = match_df.team_name.unique()

            for team_name in team_names:
                team_match_df = match_df.loc[df['team_name'] == team_name]

                data_columns = df_columns[3:]
                new_row = []
                new_row.append(str(match_id))
                new_row.append(team_name)

                new_row.append(str(round(team_match_df['kills'].mean(), 1)))

                for column_name in data_columns:
                    new_row.append(str(round(team_match_df[column_name].mean(), 1)))

                csv.write(",".join(new_row) + "\n")

print("Done.")

