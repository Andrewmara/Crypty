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