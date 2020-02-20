import csv
import sys

# Increase csv field size
csv.field_size_limit(sys.maxsize)

messages = []
symbols = []

# Load top 25 symbols from csv into  list
with open('Data/TopAppearancesOld.csv', newline='') as messageCSVFile:
    messageFile = csv.reader(messageCSVFile, delimiter=',', quotechar='|')
    for row in messageFile:
        symbols.append(row[0])

#Loading messages into a list
with open('Data/CleanedMessages.csv', newline='') as messageCSVFile:
    messageFile = csv.reader(messageCSVFile, delimiter=',', quotechar='|')
    messageFile = list(messageFile)
    del (messageFile[0])
    for row in messageFile:
        print(row[0])
        for symbol in symbols:
            dateWords = [row[0]]
            for i in range(1, row.__len__()):
                if row[i] == symbol:
                    halfArrSize = 10
                    lowerBound = max(0,i-halfArrSize)
                    upperBound = min(row.__len__(),i+(2*halfArrSize)-(i-lowerBound))
                    lowerBound = max(0, upperBound-(2*halfArrSize)-1)
                    symbolWords = [symbol]
                    for j in range(lowerBound,upperBound):
                        if j != i:
                            symbolWords.append(row[j])
                    dateWords.append(symbolWords)
            if len(dateWords) > 1:
                messages.append(dateWords)


with open('Data/SymbolMessages.csv', 'w') as f:
    for message in messages:
        line = message[0] + ','
        print(message[0])
        for i in range(1,message.__len__()):
            column = message[i]
            sentence = ''
            for element in column:
                sentence = sentence + str(element) + ' '
            line = line + str(sentence) + ','
        f.write("%s\n" % line)
