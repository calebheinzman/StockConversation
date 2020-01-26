import csv

# Loading messages into a list
import string

table = str.maketrans('', '', string.punctuation)

document = []

with open('Data/CleanedMessages.csv', newline='') as messageCSVFile:
    messageFile = csv.reader(messageCSVFile, delimiter=',', quotechar='|')
    for row in messageFile:
        print(row[0])
        lines = ''
        for i in range(1, row.__len__()):
            words = row[i].split(" ")
            words = [w.translate(table) for w in words]
            words = [word.lower() for word in words]
            for word in words:
                lines = lines + word + ' '
        document.append(lines)
print(document)

#Write all symbols and their counts to csv
with open('Data/GloveTrainingDocument.txt', 'w') as f:
    for line in document:
        line = line + '\n'
        f.write(line)