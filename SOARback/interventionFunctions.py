import sqlite3
import os
from definitions import ROOT_DIR
import json

db = os.path.join(ROOT_DIR, 'SOARback/db/SOARback_interventions.db')
interventionsTable = 'PERFORMED_INTERVENTIONS'
typesTable = 'INTERVENTION_TYPES'
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
    query = (
        f'SELECT {interventionsTable}.id, {typesTable}.name,'
        + f' {interventionsTable}.worker, {interventionsTable}.time,'
        + f'{interventionsTable}.direction, {interventionsTable}.pain_level,'
        + f'{interventionsTable}.satisfaction_level'
        + f' FROM {interventionsTable}'
        + f' JOIN {typesTable} ON {interventionsTable}.type={typesTable}.id'
        + f' ORDER BY datetime({interventionsTable}.time) DESC LIMIT {num}'
    )
    conn = connect()
    out = conn.execute(query)
    formatted = []
    for row in out:
        element = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
        print(element)
        formatted.append(element)
    disconnect(conn)
    return formatted

def getInterventionTypes():
    query = (
        f'SELECT * FROM {typesTable}'
    )
    conn = connect()
    out = conn.execute(query)
    results = []
    for row in out:
        results.append([row[0], row[1]])
    print(results)
    return results