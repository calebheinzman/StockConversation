import csv
import string
import sys
from bdateutil import isbday
from datetime import datetime, date, timedelta
from dateutil.parser import parse

# day = datetime.strptime("21/12/2008", "%d/%m/%Y")
# today = datetime.now()
# print(today.year)
# print(day.year)


# now = datetime.now()
# print(now)
# val = isbday(date(now.year, now.month, now.day))
# print(date(now.year, now.month, now.day))
# print (val)
#
# # Increase csv field size
csv.field_size_limit(sys.maxsize)
#
# messages = []
dates = []

# Load Dates Stock Market is open
with open('Data/Dates.csv', newline='') as datesCSVFile:
    datesFile = csv.reader(datesCSVFile, delimiter=',', quotechar='|')
    for row in datesFile:
        try:
            date = row[0].split("\ufeff")[1]
        except:
            date = row[0]
        day = datetime.strptime(date, "%m/%d/%y")
        day = day.replace(hour=8, minute=0, second=0)
        dates.append([day])

# Load Messages
with open('Data/messages.csv', newline='') as messageCSVFile:
    messageFile = list(messageCSVFile)
    i = 0
    for row in messageFile:
        isDate = True
        newRow = row.split(',', 1)
        try:
            day = datetime.strptime(newRow[0], "%m/%d/%Y %H:%M:%S")
            print(day)
        except:
            isDate = False
        if isDate:
            # print('isDate')
            for i in range(i,dates.__len__()-1):
                # print('inLoop')
                # print(dates[i][0])
                if (day < dates[i][0]) and (day > dates[i + 1][0]):
                    dates[i].append(newRow[1])
                    # print(i)
                    # print('inIF')
                    i = i - 10
                    break
                if i > 470:
                    i = 0


#Write all symbols and their counts to csv
with open('Data/CombinedMessages.csv', 'w') as f:
    for date in dates:
        line = ''
        for column in date:
            try:
                column = column.rstrip("\n\r")
            except:
                # print('W: '+ str(column))
                a = 1
            line = line + str(column) + ','
        f.write("%s\n" % line)


