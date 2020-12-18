from SOARback import interventionFunctions
import sqlite3

db = 'SOARback/db/SOARback_interventions.db'
test_data = [2, 'alice', '2020-12-18 12:12:12', 'left', 3, 0]

def connection_start(table):
    conn = interventionFunctions.connect()
    conn.execute(f"DELETE FROM {table}")
    conn.commit()
    conn.close()

def connection_end(conn, table):
    conn.execute(f"DELETE FROM {table}")
    conn.commit()
    conn.close()


def test_addEntry():
    connection_start('PERFORMED_INTERVENTIONS')
    interventionFunctions.addEntry(test_data)
    conn = interventionFunctions.connect()
    out = conn.execute("SELECT worker, satisfaction_level FROM PERFORMED_INTERVENTIONS")
    for row in out:
        worker = row[0]
        satisfaction = row[1]
    assert worker == test_data[1]
    assert satisfaction == test_data[5]
    connection_end(conn, 'PERFORMED_INTERVENTIONS')

def test_readLines():
    connection_start('PERFORMED_INTERVENTIONS')
    interventionFunctions.addEntry([2, 'd', '2020-12-20 12:12:12.000', 'left', 3, 0])
    interventionFunctions.addEntry([2, 'b', '2020-12-18 12:12:12.000', 'left', 3, 0])
    interventionFunctions.addEntry([2, 'c', '2020-12-18 12:12:13.000', 'left', 3, 0])
    interventionFunctions.addEntry([2, 'a', '2020-12-16 12:12:11.000', 'left', 3, 0])
    out = interventionFunctions.readLines(3)
    assert out[2][2] ==  'b'
    assert out[1][3] == '2020-12-18 12:12:13.000'
