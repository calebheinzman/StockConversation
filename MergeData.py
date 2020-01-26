import pickle
from datetime import datetime

stockData = {}

infile = open("Data/EncodedMessage.pkl",'rb')
messages = pickle.load(infile)
infile.close()

infile = open("Data/StockData.pkl",'rb')
stockData = pickle.load(infile)
infile.close()

del messages[0]

# for i in range(messages.__len__()):
#     row = messages[i]
#     date = datetime.strptime(row[0], "%m-%d-%y")
#     date = datetime.strftime(date, "%Y-%m-%d")
#     newData = stockData[date]
#     messages[i].insert(1,newData)
#     print(date)

f = open('Data/StockData.pkl','wb')
pickle.dump(messages,f)
f.close()

