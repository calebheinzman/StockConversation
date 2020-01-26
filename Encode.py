import csv
import pickle
import re
import string
from datetime import datetime

table = str.maketrans('','', string.punctuation)
messages = []
embeddings = {}

infile = open("Data/dictionary.pkl",'rb')
embeddings = pickle.load(infile)
infile.close()

with open('Data/SymbolMessages.csv', encoding="utf8", newline='') as messageCSVFile:
    messageFile = csv.reader(messageCSVFile, delimiter=',', quotechar='|')
    for row in messageFile:
        row[0] = datetime.strptime(row[0], "%m/%d/%y %H:%M")
        row[0] = datetime.strftime(row[0], "%m-%d-%y")
        print(row[0])
        datum = [row[0]]
        for i in range(1,row.__len__()):
            sentence = []
            words = row[i].split(" ")
            words = [w.translate(table) for w in words]
            words = [word.lower() for word in words]
            words = list(filter(lambda s: any([re.search('[a-zA-Z]', c) for c in s]), words))
            for word in words:
                vector = embeddings[word]
                sentence.append(vector)
            datum.append(sentence)
        messages.append(datum)



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

f = open('Data/Data.pkl','wb')
pickle.dump(messages,f)
f.close()
