# EODHistorical Data - for data fetching

import json
import pandas as pd
import requests

def get_exchange_data(key,exchange):
    
    endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/"
    endpoint = endpoint + f"{exchange}?api_token={key}&fmt=json"
    
    print("Downloading Data")
    call = requests.get(endpoint).text
    exchange_data = pd.DataFrame(json.loads(call))   
    print("Download Complete") 
    return exchange_data


def main():
    key = open('api_token.txt').read()
    df = get_exchange_data(key)
    
    df.to_csv('nyse_data.csv',index=False)
    print('Saved as NYSE Data')    

if __name__ ==  '__main__':
    main()      