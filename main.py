import csv
import json

def assign_elev(time, src, dest):
    return 0


with open(r'C:\Users\yahal\PycharmProjects\Ex1\Ex1_Buildings/B1.json') as f:
    building = json.load(f)

with open(r'C:\Users\yahal\PycharmProjects\Ex1\Ex1_Calls/Calls_a.csv') as f:
    calls = csv.reader(f)
    rows = []
    rows.append(next(calls))
    for row in calls:
        rows.append(row)
print(rows[0])
elevators = []
for i in len(rows):
    rows[i][5] = assign_elev(row[1], row[2], row[3])

