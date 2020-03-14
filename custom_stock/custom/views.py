from django.shortcuts import render
import requests
import pandas

#import alpha_vantage
#import json

def index(request):
  #  url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=B8NBTTO7NBECLIQW"
 
   # symbol = ['AIG']

   # symbol_data = requests.get(url.format(symbol)).json()

   # stock = {
     #   'function':'TIME_SERIES_INTRADAY',
      #  "symbol": symbol,
       # "interval": "60min",
      #  "datatype": "json",
       # "apikey": "B8NBTTO7NBECLIQW"

    #}
    #API_URL = "https://www.alphavantage.co/query" 
    #symbol = 'SMBL'

   # data = { "function": "TIME_SERIES_DAILY", 
   # "symbol": symbol,
   # "outputsize" : "full",
   # "datatype": "json", 
   # "apikey": "B8NBTTO7NBECLIQW" } 

   # response = requests.get(API_URL, data) 
    #response_json = response.json() 

   # data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient= 'index').sort_index(axis=1)
   # data = data.rename(columns={ '1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. adjusted close': 'AdjClose', '6. volume': 'Volume'})
   # data = data[[ 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume']]
   # data.tail() 
#for symbol in symbols:
#'AIG',"F","FB", "GOOGL", "IBM", "M","MSFT", "RDS-A"]
        #data = { "function": "TIME_SERIES_INTRADAY", 
        #"symbol": symbol,
        #"interval" : "60min",       
        #"datatype": "json", 
        #"apikey": "B8NBTTO7NBECLIQW" } 
        #response = requests.get(API_URL, data) 
        #response_json = response.json()
        #data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient= 'index').sort_index(axis=1)
        #data = data.rename(columns={ '1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. adjusted close': 'AdjClose', '6. volume': 'Volume'})
        #data = data[[ 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume']]
        #data.tail()
    
    
    #context = {'stock': stock}
    return render(request, 'custom/index.html')
