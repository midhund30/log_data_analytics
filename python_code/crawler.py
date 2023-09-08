'''
Created on 10-Apr-2022

@author: midhun
'''
import pandas as pd

df = pd.read_csv("all_data.csv", low_memory = False)
df1=pd.read_csv("UserIP.csv", low_memory = False)
ip_add = df["c-ip"].tolist()
bot = df["cs-uri-stem"].tolist()
robots_df = df[df["cs-uri-stem"].str.contains("/robots.txt", regex = False)]
robots_df["bot"] = 'robots'
print(robots_df)
robots_df = robots_df.rename({"c-ip":"IPv4"}, axis =1)
df2 = df1.merge(robots_df[["bot", "IPv4"]], how="left")
df2 = df2.drop_duplicates()
print(df2)
df2.to_csv('demp.csv',header=True)
