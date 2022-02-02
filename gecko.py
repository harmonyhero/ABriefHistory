#https://api.coingecko.com/api/v3/coins/defi-kingdoms/history?date=30-12-2021&localization=en

import requests
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
import os
from datetime import date, timedelta
import time

start_date = date(2021, 10, 8)
end_date = date(2022, 1, 31)
delta = timedelta(days=1)

while start_date <= end_date:
    #print(start_date.strftime("%d-%m-%Y"))
    sdate = start_date.strftime("%d-%m-%Y")
    url = 'https://api.coingecko.com/api/v3/coins/defi-kingdoms/history?date=' + sdate + '&localization=en'
    r = requests.get(url)
    json_data = json.loads(r.text)
    df_data = json_data['community_data']
    df = pd.json_normalize(df_data)
    df["date"] = sdate
    df['date'] = pd.to_datetime(df['date'])
    df['twitter_followers'] = df['twitter_followers'].astype(float)
    df['reddit_average_posts_48h'] = df['reddit_average_posts_48h'].astype(float)
    df['reddit_average_comments_48h'] = df['reddit_average_comments_48h'].astype(float)
    df['reddit_subscribers'] = df['reddit_subscribers'].astype(float)
    df['reddit_accounts_active_48h'] = df['reddit_accounts_active_48h'].astype(float)    
    df.fillna(0)
    start_date += delta
    time.sleep(2)
