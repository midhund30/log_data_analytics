'''
Created on 11-Apr-2022

@author: midhun
'''
import pandas as pd

df = pd.read_csv("all_data.csv", low_memory = False)
file_df = df[["cs-uri-stem","file_type"]]
file_df = file_df.drop_duplicates()
#both = file_df.append(type_df)
#a=pd.DataFrame(both)
#print(a)
print(file_df)
file_df.to_csv('file.csv',header=True)
