from cryptocmd import CmcScraper
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression

cryp = input("Inserisci crypto")

sns.set()
plt.style.use('seaborn-whitegrid')

scraper = CmcScraper(f"{cryp}")

headers, data = scraper.get_data()

xrp_json_data = scraper.get_data("json")

scraper.export("csv", name = f"data-set/{cryp}_all_time")

df = scraper.get_dataframe()



data = pd.read_csv(f"data-set/{cryp}_all_time.csv")
print("Shape of Dataset is: ",data.shape,"\n")
print(data.head())

data.dropna()
plt.figure(figsize=(10, 4))
plt.title("SOL Price INR")
plt.xlabel("Date")
plt.ylabel("Close")
plt.plot(data["Close"])
plt.show()


