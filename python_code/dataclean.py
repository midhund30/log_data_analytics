'''
Created on 08-Apr-2022

@author: midhun
'''
import os
import pandas as pd

#os.getcwd()
data_folder = os.path.join(os.getcwd(),'data')

list(os.walk(data_folder))

print(len(list(os.walk(data_folder))[0]))
print(list(os.walk(data_folder))) 


data =[]
keys = ("date", 
"time",
"s-ip", 
"cs-method", 
"cs-uri-stem", 
"cs-uri-query",
"s-port",
"cs-username", 
"c-ip", 
"cs(User-Agent)",
"sc-status",
"sc-substatus", 
"sc-win32-status",
"time-taken")
for root, folders, files in os.walk(data_folder):
    for file in files:
        path= os.path.join(root,file)
        for inf in open(path):
            line = inf.strip()
            if not line.startswith("#"):
                val = line.split(" ")
                val = [x.strip() for x in val]
                data.append(val)
                
print(data[0:100])
#df = pd.DataFrame(data)
#df.drop(df.columns[[15,16,17,18,19,20,21,22,23,24,25,26]],axis=1)
df = pd.DataFrame(data)
df.drop(df.columns[[15,16,17,18,19,20,21,22,23,24,25,14]], axis = 1, inplace = True)
#df= df.head()
df.columns = ["date", 
"time",
"s-ip", 
"cs-method", 
"cs-uri-stem", 
"cs-uri-query",
"s-port",
"cs-username", 
"c-ip", 
"cs(User-Agent)",
"sc-status",
"sc-substatus", 
"sc-win32-status",
"time-taken"]

df.to_csv('all_data.csv',header=True)



