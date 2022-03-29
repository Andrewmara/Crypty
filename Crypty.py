
from cryptocmd import CmcScraper
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression
import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from IPython.display import display
import pandas as pd
from autots import AutoTS

cryp = input("Inserisci crypto: ")
sns.set()
plt.style.use('seaborn-whitegrid')
scraper = CmcScraper(f"{cryp}")
headers, data = scraper.get_data()
json_data = scraper.get_data("json")
scraper.export("csv", name=f"data-set/{cryp}_all_time")

df = scraper.get_dataframe()


data = pd.read_csv(f"data-set/{cryp}_all_time.csv")
print("Shape of Dataset is: ", data.shape, "\n")
print(data.head())


model = AutoTS(forecast_length=15, frequency='infer', ensemble='simple', drop_data_older_than_periods=200)
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)
 
prediction = model.predict()
forecast = prediction.forecast
print(f"{cryp} Prediction")
print(forecast)

