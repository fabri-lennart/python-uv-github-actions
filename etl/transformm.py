# this script read the data from data directory and then process it using duckdb
import pandas as pd
import json

# pandas dataframe with  columns filtered
df = pd.json_normalize(json.load(open('data/user_data.json')))

#  save the dataframe as a csv fike 
df.to_csv('data/user_data_processed.csv', index=False)
