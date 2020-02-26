import csv
import pickle
import re
import string
from datetime import datetime

import numpy as np

table = str.maketrans('','', string.punctuation)
messages = {}
embeddings = {}

f = open('Data/vectors.txt', 'r')
embeddings = {}
for line in f:
    splitLine = line.split()
    word = splitLine[0]
    embedding = np.array([float(val) for val in splitLine[1:]])
    embeddings[word] = embedding


# infile = open("Data/dictionary.pkl",'rb')
# embeddings = pickle.load(infile)
# infile.close()

with open('Data/SymbolMessages.csv', encoding="utf8", newline='') as messageCSVFile:
    messageFile = csv.reader(messageCSVFile, delimiter=',', quotechar='|')
    for row in messageFile:
        row[0] = datetime.strptime(row[0], "%m/%d/%y %H:%M")
        row[0] = datetime.strftime(row[0], "%m-%d-%y")
        print(row[0])
        date = row[0]
        try:
            messages[date] = messages[date]
        except:
            messages[date] = {}
        datum = []
        for i in range(1,row.__len__()-1):
            words = row[i].split(" ")
            symbol = words[0]
            sentence = []
            words = [w.translate(table) for w in words]
            words = [word.lower() for word in words]
            words = list(filter(lambda s: any([re.search('[a-zA-Z]', c) for c in s]), words))
            for word in words:
                try:
                    vector = embeddings[word]
                    sentence.append(vector)
                except:
                    pass
            datum.append(sentence)
        messages[date][symbol] = datum



    # for message in messages:
    #     with open('Data/EncodedMessages/'+message[0]+'.csv', 'w') as f:
    #         print(message[0])
    #         for i in range(1,message.__len__()):
    #             column = message[i]
    #             line = ''
    #             for element in column:
    #                 line = line + str(element) + ','
    #             f.write("%s\n" % line)
    #     f.close

f = open('Data/DataDictionaryCustom200D.pkl','wb')
pickle.dump(messages,f)
f.close()
