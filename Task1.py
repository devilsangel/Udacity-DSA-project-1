"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
numberSet=set([])
for call in calls:
    numberSet.add(call[0])
    numberSet.add(call[1])

for text in texts:
    numberSet.add(text[0])
    numberSet.add(text[1])

print("There are %s different telephone numbers in the records." % len(numberSet))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
