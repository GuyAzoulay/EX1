import csv
import json
from Building import *
from Elevator import *
from calls import  *
import sys


def loadJson(fileName):
    try:
        with open(fileName, 'r') as f:
            building = json.load(f)
            return building
    except IOError as e:
        print(e)
        return building


def loadCsv(fileName):
    with open(fileName) as f:
        calls = csv.reader(f)
        rows = []
        rows.append(next(calls))
        print(type(rows[0]))
        print(rows[0][0])
        for row in calls:
            rows.append(row)
    return rows


def allocateElev(building:Building, calls:Calls):
    build = loadJson(building)
    call = loadCsv(calls)
    ind = 0
    time = sys.maxsize




if __name__ == '__main__':
    build = loadJson("B2.json")
    building= Building(build)
    print(type(building))
    calls = loadCsv("Calls_a.csv")
    print(calls)
    for i in  range(len(calls)):
        calls[i][5] = building.__add__(calls[i])
    print(calls)


