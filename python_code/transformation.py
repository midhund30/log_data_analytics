'''
Created on 10-Apr-2022

@author: midhun
'''

import pandas as pd

df = pd.read_csv("all_data.csv", low_memory = False)
a= df.date.unique()
a=pd.DataFrame(a)
a.columns =["date"]
a.to_csv('date.csv',header=True)
print(a)
