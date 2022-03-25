from cryptocmd import CmcScraper

# initialise scraper without time interval
scraper = CmcScraper("SOL")

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
xrp_json_data = scraper.get_data("json")

# export the data as csv file, you can also pass optional `name` parameter
scraper.export("csv", name="xrp_all_time")

# Pandas dataFrame for the same data
df = scraper.get_dataframe()

"""""
from cryptocmd import CmcScraper

# initialise scraper with time interval
scraper = CmcScraper("XRP", "15-10-2017", "25-10-2017")

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
json_data = scraper.get_data("json")

# export the data to csv
scraper.export("csv")

# get dataframe for the data
df = scraper.get_dataframe()
"""

from cryptocmd import CmcScraper
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression

cryp = input("Inserisci crypto")

sns.set()
plt.style.use('seaborn-whitegrid')
# initialise scraper without time interval
scraper = CmcScraper(f"{cryp}")

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
xrp_json_data = scraper.get_data("json")

# export the data as csv file, you can also pass optional `name` parameter
scraper.export("csv", name="data-set/SOL_all_time")

# Pandas dataFrame for the same data
df = scraper.get_dataframe()



data = pd.read_csv("data-set/{cryp}.csv")
print("Shape of Dataset is: ",data.shape,"\n")
print(data.head())

data.dropna()
plt.figure(figsize=(10, 4))
plt.title("SOL Price INR")
plt.xlabel("Date")
plt.ylabel("Close")
plt.plot(data["Close"])
plt.show()

