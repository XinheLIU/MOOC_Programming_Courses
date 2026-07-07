# -*- coding: utf-8 -*-
"""
the k-Means Algorithm

@author: Dazhuang
"""

# you can understand this program instead of running it for the website's load 
# result(may change): [2 2 1 1 2 2 2 2 0 0]

import requests
import re
import json
import pandas as pd
from sklearn.cluster import KMeans 
import numpy as np


def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

def create_df(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = ['close','date','high','low','open','volume']
    df_totalvolume = pd.DataFrame(quotes,columns=list1)
    # replace the NaN values(missing values) with the mean
    df_totalvolume = df_totalvolume.fillna(df_totalvolume.mean())
    return df_totalvolume
    
    
listDji = ['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DD']
listTemp = [0] * len(listDji)
for i in range(len(listTemp)):
    listTemp[i] = create_df(listDji[i]).close
status = [0] * len(listDji)
for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
# fail to crawl the data of some stocks(the value is []), drop it 
for i in range(len(status)):
    if len(status[i]) == 0:
		     status.pop(i)
		     break
kmeans = KMeans(n_clusters = 3).fit(status)
pred=kmeans.predict(status)
print(pred)