from SOARback import csvFunctions
import os
import csv

dataLocation = 'data.txt'
fields = ['time', 'date', 'action', 'risk']
testData = ['a', 'aa', 'aaa', 'aaaa']

def test_fileCreated():
    os.remove(dataLocation)
    csvFunctions.initCsv()
    assert os.path.exists('data.txt') == True

def test_ColumnCreation():
    data = []
    csvFunctions.initCsv()
    with open(dataLocation, 'r+') as csvfile:
        csvRows = csv.reader(csvfile, delimiter=';')
        for row in csvRows:
            if row:
                columns = [row[0], row[1], row[2], row[3]]
                data.append(columns)
    assert data[0] == fields

def test_dataWrite():
    data = []
    csvFunctions.addEntry([testData])
    with open(dataLocation, 'r+') as csvfile:
        csvRows = csv.reader(csvfile, delimiter=';')
        for row in csvRows:
            if row:
                columns = [row[0], row[1], row[2], row[3]]
                data.append(columns)
    assert data[1] == testData

# todo, more stuff with edge cases. 
# - less than enough entries available

def test_dataRead():
    with open(dataLocation, 'a+') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerows([testData])
    out = csvFunctions.readLines(1)
    assert out == [testData]