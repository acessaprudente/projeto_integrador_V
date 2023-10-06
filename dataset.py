import json, requests
import pandas as pd
from datetime import date, datetime
from pandas import json_normalize

file = open('dados/feeds.json')
data = json.load(file)
df = pd.DataFrame.from_dict(data['feeds'])
df['created_at'] = pd.to_datetime(df['created_at'], format="%Y/%m/%d %H:%M:%S", exact=False, dayfirst=True, errors='ignore')
 
















