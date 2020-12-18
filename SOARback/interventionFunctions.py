# - read # of lines
# - add a line

import sqlite3
import os
from definitions import ROOT_DIR

db = os.path.join(ROOT_DIR, 'SOARback/db/SOARback_interventions.db')
interventionsTable = 'PERFORMED_INTERVENTIONS'
allColumns = '(id, type, worker, time, direction, pain_level, satisfaction_level)'
insertColumns = '(type, worker, time, direction, pain_level, satisfaction_level)'

def connect():
    conn = sqlite3.connect(db)
    return conn

def disconnect(conn):
    conn.commit()
    conn.close()

def addEntry(contents):
    query = (f'INSERT INTO {interventionsTable}'
    + f' {insertColumns}'
    + f' VALUES ({contents[0]}, \'{contents[1]}\','
    + f' \'{contents[2]}\', \'{contents[3]}\','
    + f' {contents[4]}, {contents[5]})')
    conn = connect()
    conn.execute(query)
    disconnect(conn)
    return 1

def readLines(num):
    query = (f'SELECT *'
    + f' from {interventionsTable}'
    + f' ORDER BY datetime(time) DESC LIMIT {num}')
    conn = connect()
    out = conn.execute(query)
    formatted = []
    for row in out:
        element = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
        formatted.append(element)
    disconnect(conn)
    print(formatted)
    return formatted
