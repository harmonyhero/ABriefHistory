import requests
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
import os

endnum = 1
lastnum = int()

while endnum <= 500:
 
  if endnum == 1:
    valx = 1643377529
  else:
    valx = lastnum - 10
  
  print(valx)
  query = """query {
    saleAuctions(orderBy: endedAt, first: 1000, orderDirection: desc, where:{open: false, purchasePrice_not: null, endedAt_lte:""" + str(valx) + """}) {
    id
    endedAt
    open
    endingPrice
    purchasePrice
    tokenId {
      numberId
      mainClass
      subClass
      profession
      rarity
      generation
      level
      statBoost1
      statBoost2
      
    }
  }
}"""

  url = 'http://graph3.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'
  r = requests.post(url, json={'query': query})
  json_data = json.loads(r.text)
  df_data = json_data['data']['saleAuctions']
  df = pd.json_normalize(df_data)
  #print(df)
  df = df.sort_values(by=['endedAt'], ascending=False)

  df["endingPrice"] = pd.to_numeric(df["endingPrice"],errors='coerce')
  df["endingPrice"] /= 1000000000000000000
  df['tokenId.rarity'] = df['tokenId.rarity'].apply(str)

  df.loc[df['tokenId.rarity'].str.contains('0'), 'tokenId.rarity'] = 'Common'
  df.loc[df['tokenId.rarity'].str.contains('1'), 'tokenId.rarity'] = 'Uncommon'
  df.loc[df['tokenId.rarity'].str.contains('2'), 'tokenId.rarity'] = 'Rare'
  df.loc[df['tokenId.rarity'].str.contains('3'), 'tokenId.rarity'] = 'Legendary'
  df.loc[df['tokenId.rarity'].str.contains('4'), 'tokenId.rarity'] = 'Mythic'
  df.loc[df['tokenId.mainClass'].str.contains('T1'), 'tokenId.mainClass'] = 'DreadKnight'
  df.loc[df['tokenId.subClass'].str.contains('T1'), 'tokenId.subClass'] = 'DreadKnight'
  valnum = int(df["endedAt"].tail(1).values[0])
  lastnum = valnum
  endnum += 1
    

