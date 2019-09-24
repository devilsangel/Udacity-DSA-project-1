"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
callTimesSet = {}
recievingCallTimesSet = {}
for call in calls:
    if call[0] in callTimesSet:
        callTimesSet[call[0]]+=call[3]
    else:
        callTimesSet[call[0]]=call[3]
    if call[1] in recievingCallTimesSet:
        recievingCallTimesSet[call[1]]+=call[3]
    else:
        recievingCallTimesSet[call[1]]=call[3]

longestTime = calls[0][3]
longestCaller = calls[0][1]

for call in callTimesSet:
    if(callTimesSet[call]>longestTime):
        longestTime = callTimesSet[call]
        longestCaller = call

for call in recievingCallTimesSet:
    if(recievingCallTimesSet[call]>=longestTime):
        longestTime = recievingCallTimesSet[call]
        longestCaller = call

print("%s spent the longest time, %s seconds, on the phone during September 2016." % (longestCaller, longestTime))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

