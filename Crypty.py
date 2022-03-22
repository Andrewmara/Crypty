import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint 



#API----------------------------------------------------------------------------
pp = pprint.PrettyPrinter(indent=4)
url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
print(url)

symbolstr=','.join(('BTC,ETH,BNB,XRP,USDT,ADA,DOT,UNI,LTC,LINK,XLM,BCH', 
        'THETA,FIL,USDC,TRX,DOGE,WBTC,VET,SOL,KLAY,EOS,XMR,LUNA', 
        'MIOTA,BTT,CRO,BUSD,FTT,AAVE,BSV,XTZ,ATOM,NEO,AVAX,ALGO', 
        'CAKE,HT,EGLD,XEM,KSM,BTCB,DAI,HOT,CHZ,DASH,HBAR,RUNE,MKR,ZEC',
        'ENJ,DCR,MKR,ETC,GRT,COMP,STX,NEAR,SNX,ZIL,BAT,LEO,SUSHI', 
        'MATIC,BTG,NEXO,TFUEL,ZRX,UST,CEL,MANA,YFI,UMA,WAVES,RVN',
        'ONT,ICX,QTUM,ONE,KCS,OMG,FLOW,OKB,BNT,HNT,SC,DGB,RSR,DENT',
        'ANKR,REV,NPXS,VGX,FTM,CHSB,REN,IOST,CELO,CFX'))
symbol_list=symbolstr.split(',')
cryptoapi = "25d7a041-3177-4167-84ca-e8c5748eda49"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cryptoapi,
}
parameters = {
  'symbol':symbolstr
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


if(data['data']['SOL']['name'] == "Solana"):
  thename=data['data']['SOL']['name']
  sym = data['data']['SOL']['symbol']
  price = data['data']['SOL']['quote']['USD']['price']
  print(thename + ", " + sym + ", " + str(price))
