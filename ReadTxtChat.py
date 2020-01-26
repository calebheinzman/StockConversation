# The purpose of this file is to extract the message and date from a Discord JSON and write them to a csv fil.

import json
import time

# Keeps track of all messages
messages = []
# Name of file with messages
fileName = 'Data/dht.txt'

# Read TXT file
with open(fileName) as json_file:
    # Converts txt file to JSON
    data = json.load(json_file)
    #Loop through data kfield
    for chat in data['data']:
        #Loop through all messages

        for message in data['data'][chat]:
            try:
                date = data['data'][chat][message]['t']
                date = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(date / 1000.))
                message = data['data'][chat][message]['m']
                messages.append([date,message])
            except:
                print(message)

#Writes messages to csv
with open('Data/messages.csv', 'w') as f:
    for message in messages:
        line = str(message[0]) + ',' + str(message[1])
        f.write("%s\n" % line)
