import pandas as pd

pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', 50)

csv_path = '130k_cln.csv'

# df_columns = pd.read_csv(csv_path, nrows=1, index_col=False,)

df_columns = ['match_id', 'team_name', 'player_name', 'kills', 'headshots', 'assists', 'flash_assists', 'deaths',
              'kd_ratio', 'kd_diff', 'adr', 'fk_dif', 'rating']

df = pd.read_csv(csv_path, names=df_columns, skiprows=1, index_col=False, skipinitialspace=True)

matches = df.match_id.unique()

match_df = df.loc[df['match_id'] == 65393]

desc_columns = df_columns[:3]
data_columns = df_columns[3:]
new_row = []
for column_name in desc_columns:
    new_row.append(match_df[column_name].iloc[0])

for column_name in data_columns:
    new_row.append(round(match_df[column_name].mean(), 1))

print(new_row)



# mean_k = round(match_df['kills'].mean(), 1)
# mean_hs = round(match_df['headshots'].mean(), 1)
# mean_a = round(match_df['assists'].mean(), 1)
# mean_fa = round(match_df['flash_assists'].mean(), 1)
# mean_d = round(match_df['deaths'].mean(), 1)
# mean_kdr = round(match_df['kd_ratio'].mean(), 1)
# mean_kdd = round(match_df['kd_diff'].mean(), 1)
# mean_adr = round(match_df['adr'].mean(), 1)
# mean_fkd = round(match_df['fk_dif'].mean(), 1)
# mean_r = round(match_df['rating'].mean(), 1)


# print(mean_k, mean_hs, mean_a, mean_fa, mean_d, mean_kdr, mean_kdd, mean_adr, mean_fkd, mean_r)



