import pandas as pd

# pd.set_option('display.max_row', 1000)
# pd.set_option('display.max_columns', 50)

df_columns = ['match_id', 'team_name', 'player_name', 'kills', 'headshots', 'assists', 'flash_assists', 'deaths',
              'kd_ratio', 'kd_diff', 'adr', 'fk_dif', 'rating']

csv_path = '130k_cln.csv'
df = pd.read_csv(csv_path, names=df_columns, skiprows=1, index_col=False, skipinitialspace=True)

match_ids = df.match_id.unique()

with open('match_avgs.csv', 'w') as csv:
    for match_id in match_ids:
        match_df = df.loc[df['match_id'] == match_id]

        if len(match_df.index) == 10:  # Only add the match if it has the full 10 players.
            team_names = match_df.team_name.unique()
            for team_name in team_names:
                team_match_df = df.loc[df['team_name'] == team_name]

                desc_columns = df_columns[:3]
                data_columns = df_columns[3:]
                new_row = []
                for column_name in desc_columns:
                    new_row.append(str(team_match_df[column_name].iloc[0]))

                for column_name in data_columns:
                    new_row.append(str(round(team_match_df[column_name].mean(), 1)))

                csv.write(",".join(new_row) + "\n")

print("Done.")

