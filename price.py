import requests
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
import os
from datetime import date, timedelta
import time

url = 'https://api.coingecko.com/api/v3/coins/defi-kingdoms/ohlc?vs_currency=usd&days=90'
r = requests.get(url)
json_data = json.loads(r.text)
df_data = json_data
df = pd.json_normalize(df_data)
df.fillna(0)
    