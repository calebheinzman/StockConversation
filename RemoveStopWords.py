import csv
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import ssl

# Overide SSL Certificate
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download Files
nltk.download('stopwords')
nltk.download('punkt')

# Set the stop word
stopWords = set(stopwords.words('english'))

# Increase csv field size
csv.field_size_limit(sys.maxsize)

# Keep track of symbols and messages
symbols = []
messages = []

# Load all messages from csv into list
with open('Data/CombinedMessages.csv', newline='') as messageCSVFile:
    messageFile = list(messageCSVFile)
    for row in messageFile:
        newRow = row.split(',', 1)
        if newRow.__len__() > 1:
            tokenizer = nltk.RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(newRow[1])
            filteredMessage = [w for w in tokens if not w in stopWords]
            filteredMessage.insert(0,newRow[0])
            print(newRow[0])
            messages.append(filteredMessage)



with open('Data/CleanedMessages.csv', 'w') as f:
    for message in messages:
        line = ''
        for column in message:
            try:
                column = column.rstrip("\n\r")
            except:
                print('W: '+ str(column))
            line = line + str(column) + ','
        f.write("%s\n" % line)
