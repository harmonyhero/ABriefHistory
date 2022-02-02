import requests
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize
import os

endnum = 1

while endnum <= 100:
    valx = endnum * 1000
    query = """query {
  heros(orderBy: numberId, orderDirection:desc, first:1000, where:{numberId_lte:""" + str(valx) + """}) {
    numberId
    id
    mainClass
    subClass
    profession
    rarity
    generation
    statBoost1
    statBoost2
    shiny
    element
    salePrice
    gender
    summonedTime
    level
  }
}"""
    url = 'http://graph3.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)
    df_data = json_data['data']['heros']
    df = pd.DataFrame(df_data)
    df['rarity'] = df['rarity'].apply(str)
    df.loc[df['rarity'].str.contains('0'), 'rarity'] = 'Common'
    df.loc[df['rarity'].str.contains('1'), 'rarity'] = 'Uncommon'
    df.loc[df['rarity'].str.contains('2'), 'rarity'] = 'Rare'
    df.loc[df['rarity'].str.contains('3'), 'rarity'] = 'Legendary'
    df.loc[df['rarity'].str.contains('4'), 'rarity'] = 'Mythic'
    df.loc[df['mainClass'].str.contains('T1'), 'mainClass'] = 'DreadKnight'
    df.loc[df['subClass'].str.contains('T1'), 'subClass'] = 'DreadKnight'
    df = df.sort_values(by=['numberId'], ascending=True)
    endnum += 1




    
    