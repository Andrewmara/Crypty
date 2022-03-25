import os
from cryptocmd import CmcScraper
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression
import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from IPython.display import display
import pandas as pd

pp = pprint.PrettyPrinter(indent=4)
url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
print(url)
cryptoapi = "25d7a041-3177-4167-84ca-e8c5748eda49"

symbolstr = ','.join(('BTC,ETH,BNB,XRP,USDT,ADA,DOT,UNI,LTC,LINK,XLM,BCH',
                     'THETA,FIL,USDC,TRX,DOGE,WBTC,VET,SOL,KLAY,EOS,XMR,LUNA',
                      'MIOTA,BTT,CRO,BUSD,FTT,AAVE,BSV,XTZ,ATOM,NEO,AVAX,ALGO',
                      'CAKE,HT,EGLD,XEM,KSM,BTCB,DAI,HOT,CHZ,DASH,HBAR,RUNE,MKR,ZEC',
                      'ENJ,DCR,MKR,ETC,GRT,COMP,STX,NEAR,SNX,ZIL,BAT,LEO,SUSHI',
                      'MATIC,BTG,NEXO,TFUEL,ZRX,UST,CEL,MANA,YFI,UMA,WAVES,RVN',
                      'ONT,ICX,QTUM,ONE,KCS,OMG,FLOW,OKB,BNT,HNT,SC,DGB,RSR,DENT',
                      'ANKR,REV,NPXS,VGX,FTM,CHSB,REN,IOST,CELO,CFX'))
symbol_list = symbolstr.split(',')

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cryptoapi,
}
parameters = {
    'symbol': symbolstr
}
session = Session()
session.headers.update(headers)
try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print("Funziona")
    pp.pprint(data)


except (ConnectionError, Timeout, TooManyRedirects) as e:
    data = json.loads(response.text)
    print("qualcosa non va")

datacryp = {
    'Symbol': [],
    'Crypto': [],
}

df_marks = pd.DataFrame(datacryp)


for symbol in symbol_list:
    new_row = {
        'Symbol': symbol,
        'Crypto': data['data'][symbol]['name'],
    }
    df_marks = df_marks.append(new_row, ignore_index=True)

display(df_marks)
# df_marks.to_csv("data-set/cryptoList.csv")


cryp = input("Inserisci crypto: ")
sns.set()
plt.style.use('seaborn-whitegrid')
scraper = CmcScraper(f"{cryp}")
headers, data = scraper.get_data()
xrp_json_data = scraper.get_data("json")
scraper.export("csv", name=f"data-set/{cryp}_all_time")

df = scraper.get_dataframe()


data = pd.read_csv(f"data-set/{cryp}_all_time.csv")
print("Shape of Dataset is: ", data.shape, "\n")
print(data.head())

data.dropna()
plt.figure(figsize=(10, 4))
plt.title("SOL Price INR")
plt.xlabel("Date")
plt.ylabel("Close")
plt.plot(data["Close"])
plt.show()
