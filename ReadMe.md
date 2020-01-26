#Setup
pip install nump
pip install scipy
pip install matplotlib
pip install sklearn

# Summary
This project takes a conversation from a discord server extracts relevant stock info.
The conversation is extracted by using Discord History Tracker. https://dht.chylex.com

The order of programs to be run is as followed:
1. ReadTxtChat.py
2. FindSymbols.py
3. CombineMessages.py
4. RemoveWords.py
5. FindCorrespondingWords.py
6. CreateSingleDocument.py
7. Glove.py
8. Encode.py
9. OrganizeHistoricalData.py

# Pytho Programs

## ReadTxtChat.py
This program takes the text file outputted from discord history
and converts it to a csv file called 'messages.csv'. This
keeps track of each message along with the date it was sent.

## FindSymbols.py
This program takes the 'messages.csv' file and looks for
any symbol from the NASDAQ and counts it. These symbols were
retrieved from another program and are in a csv file called "symbols.csv".
This program will output an 'Appearances.csv' where the symbol 
along with the number of occurences is stored. I then manually sorted in
Excel and kept only the top 25 symbols.

### CombinedMessages.py
This file combines all messages relevant to one trading day. To
get the trading day I took the historical data from FB, and 
manually deleted all other fields. I loaded all the data from
the 'Appearances.csv' file, then checked if a message
was between 8:00am of the previous day, to 8:00am of the 
current day. If it was it was stored in the same day. This
program outputs a 'CombinedMessages.csv" file where each row
corresponds to a day, and each column is a message.

### RemoveStopWords.py
This file takes the 'CombinedMessages.py' file and removes all irrelevant words and combines all messages for
one day. This then outputs a 'CleanedMessages.csv' file where
each row corresponds to a date and each column is a single word from that date.

### FindCorrespondingWords.py
This file takes in the 'Appearances.csv' file and the 'CleanedMessages.csv'
file. Everytime a symbol appears, it records the 20 closest words to 
the symbol. It ouputs the 'SymbolMessages.csv' file. Each row corresponds to
a date and each column has a symbol and the 20 closest words to the symbol.

### CreateSingleDocument.py
This program takes the 'CleanedMessages.csv' files and 
combines all messages from each date into a single line. This
produces a 'GloveTrainingDocument.txt' file with lines of text 
corresponding to each date.

### Glove.py
Because of errors with installing the module glove on my Mac I got the following to work on windows after some struggling 
with Visual Studios (My mac needed xcode but I didnt have space to install):
https://medium.com/analytics-vidhya/basics-of-using-pre-trained-glove-vectors-in-python-d38905f356db

This program trained word embeddings based on 'GloveTrainingDocument.txt'. This program
output a dictionary.pkl file which contained the embeddings for each word.

### Encode.py
This takes the 'dictionary.pkl' file from the windows computer and uses it to produce
word embeddings for each word in the 'SymbolMessages.csv' file. It outputs an
'EncodedMessages.pkl' file with vectors instead of words. I also commented out the
part of code that could turn this into a series of CSV files.

### OrganizeHistoricalData.py
I manually downloaded historical data csv files for each stock in the 
'TopAppearances.csv' file. This program gets all the symbols from 'TopAppearances.csv' 
and uses it to loop through each csv file. This file gathers the historical data pertaining
to each financial day. It uses the previous 5 days of 'open, close, high and low' values
and associates it with that day. It does this for each stock and stores it under a
dictionary for that date. Originally I had it use the actual closing price of that day
as a label, but I decided to use a 0 or 1 if the closing price increased from the previous 
day (this is commented out though). This file outputs a 'StockData.pkl' and 'Labels.pkl' files
with both dictionaries stored. I changed the names for the adjustments I made.

### MergeData.py
Originally I planned on using the historical data for training but I realized that 
this would probably not work. This program originally loaded 'EncodedMessages.pkl' and
'StockData.pkl' and merged the two so that each date had associated messages and historical 
prices. It would store this in 'MergedData.pkl'. However, I decided not to do this so I 
commented out the bulk of this code and just used it to remove the first row of messages so it
would line up with the stocks labels from their csv files.


## Notes:
I have transitioned to windows for training the LSTM.
I have first decided to remove all historical stock data
from the messages. The labels will be either 0 or 1 depending
on if the close price increased from the previous day.
I have divided the data into testing and training data at
80% - 20%. Next step is to train LSTM.

## Improvement Ideas

- Currenty I am training an LSTM to predict for all
stocks at once. It might be better to train an LSTM for 
each stock individually.
- Go to other discords and get more data.
- Use % Increase instead of just 0 or 1 labels.
- Incorporate historical data somehow. The current problem with 
using historical data is that it is in a different format than 
all of the words.
- Change the number of words used in corresponding to
each symbol.
- Use every message in a day.

## If successful
Use LSTM trained on conversations in conjunction
withj other models trained on different data as input
for deep Q-learning agent.