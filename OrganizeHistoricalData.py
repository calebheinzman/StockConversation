import csv
import pickle

symbols = []
historicalData = {}
allLabels = {}

# Load top 25 symbols from csv into  list
with open('Data/TopAppearancesOld.csv', newline='') as symbolCSVFile:
    symbolFile = csv.reader(symbolCSVFile, delimiter=',', quotechar='|')
    for row in symbolFile:
        symbols.append(row[0])
downCount = 0
upCount = 0
for symb in symbols:
    fileName = 'Data/StockData/' + symb + '.csv'
    with open(fileName, newline='') as historicalDataCSVFile:
        historicalDataFile = csv.reader(historicalDataCSVFile, delimiter=',', quotechar='|')
        historicalDataFile = list(historicalDataFile)
        numDataPoints = 5
        for i in range(historicalDataFile.__len__()-1,numDataPoints,-1):
            date = historicalDataFile[i][0]
            row = historicalDataFile[i-numDataPoints:i]
            line = []
            # label = [historicalDataFile[i][4]]
            dataClose = [historicalDataFile[i][4]]
            dataPreviousClose = [historicalDataFile[i-1][2]]
            if dataClose > dataPreviousClose:
                label = 1
                upCount = upCount + 1
            else:
                label = 0
                downCount = downCount + 1
            for j in range(numDataPoints):
                line.append([row[j][k] for k in [1,2,3,4,6]])
            try:
                historicalData[date].append(line)
                allLabels[date].append(label)
            except:
                historicalData[date]= [line]
                allLabels[date] = [label]



    print(date)
    print(symb)
    # print(allLabels)
    # print(historicalData)

print(upCount)
print(downCount)
print(str(upCount/(downCount+upCount)))

f = open('Data/StockData.pkl','wb')
pickle.dump(historicalData,f)
f.close()
f = open('Data/Labels.pkl','wb')
pickle.dump(allLabels,f)
f.close()