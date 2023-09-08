import requests
import pandas as pd
import json

df = pd.read_csv("all_data.csv", low_memory = False)
url = 'https://geolocation-db.com/jsonp/'


ip_add = df["c-ip"].unique().tolist()
#print(len(ip_add))


ip_out_list = []
for ip in ip_add:
    resp = requests.get(url + ip)
    op = resp.content.decode()
    op = op.split("(")[1].strip(")")
    op = json.loads(op)
    print(op)
    ip_out_list.append(op)

ip_out_df = pd.DataFrame(ip_out_list,columns = ['IPv4','country_code','country_name','state','city','postal','latitude','longitude'])
print(ip_out_df)
ip_out_df.to_csv('UserIP.csv',header=True)



