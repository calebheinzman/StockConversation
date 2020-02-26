import csv
from datetime import datetime
import pandas_datareader.data as web

with open('Data/messages.csv', newline='') as messageCSVFile:
    messageFile = list(messageCSVFile)
    day = messageFile[0].split(',', 1)[0]
    day = datetime.strptime(day, "%m/%d/%Y %H:%M:%S")
    lastDay = datetime.strftime(day, "%Y-%m-%d")
    day = messageFile[messageFile.__len__()-1].split(',', 1)[0]
    day = datetime.strptime(day, "%m/%d/%Y %H:%M:%S")
    firstDay = datetime.strftime(day, "%Y-%m-%d")

# Load top 25 symbols from csv into  list
symbols = []
with open('Data/TopAppearancesOld.csv', newline='') as messageCSVFile:
    messageFile = csv.reader(messageCSVFile, delimiter=',', quotechar='|')
    for row in messageFile:
        symbols.append(row[0])
for symb in symbols:
    # Get the data from quandl
    data = web.DataReader(symb, 'yahoo', firstDay, lastDay)
    data.to_csv("Data/StockData/"+symb+".csv")

    print(symb)


