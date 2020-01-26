#The purpose of this file is to count how many times a symbol appears in all of the messages.

import csv
import sys

# Increase csv field size
csv.field_size_limit(sys.maxsize)

#Keeps track of symbols and messages
messages = []
symbols = []

#Loading messages into a list
with open('Data/messages.csv', newline='') as messageCSVFile:
    messageFile = csv.reader(messageCSVFile, delimiter=' ', quotechar='|')
    for row in messageFile:
        messages.append(row)

#Loading Symbols Into a list
with open('Data/symbolFile.csv', newline='') as symbolCSVFile:
    symbolFile = csv.reader(symbolCSVFile, delimiter=',', quotechar='|')
    for row in symbolFile:
        symbols.append([row[0],0])

#Loop through messages and find a symbol.
#Everytime the symbol is found, increase the count by one
for row in messages:
    for element in row:
        for i in range(0,symbols.__len__()):
            symb = symbols[i][0]
            if symb == element:
                symbols[i][1] = symbols[i][1] + 1
                print(row[0])

#Write all symbols and their counts to csv
with open('Data/appearances.csv', 'w') as f:
    for symb in symbols:
        print(symb)
        line = symb[0] + ',' + str(symb[1])
        f.write("%s\n" % line)