import os
import csv

fields = ['time', 'date', 'action', 'risk']
filename = 'data.txt'

def initCsv():
    if not os.path.exists(filename):
        with open(filename, 'w+') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';')
            csvwriter.writerow(fields)
    return 0

def readLines(number):
    data = []
    out = []
    with open(filename, 'r') as csvfile:
        csvRows = csv.reader(csvfile, delimiter=';')
        for row in csvRows:
            if row:
                columns = [ row[0], row[1], row[2], row[3]]
                data.append(columns)
        if len(data) < number:
            number = len(data)
        for num in range(1, number + 1):
            out.append(data[-1 * num])
    return out
    

def addEntry(contents):
    with open(filename, 'a+') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerows(contents)
    return 0