'''
Created on 11-Apr-2022

@author: midhun

'''

import pandas as pd

df = pd.read_csv("all_data.csv", low_memory = False)
fact_df = df[["date","c-ip","cs-method","cs-uri-stem","file_type","sc-status"]]
print(fact_df)
fact_df.to_csv('fact1.csv',header=True)