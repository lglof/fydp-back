from SOARback import passFunctions
import os
import sqlite3
from definitions import ROOT_DIR

db = 'SOARback/db/SOARback_users.db'

# def test_initSecurity_new_password():
#     open(passFile, 'w+').close()
#     passFunctions.generatePassword('1234')
#     assert passFunctions.verify('1234') == True

def connection_start(table):
    conn = sqlite3.connect(db)
    conn.execute(f"DELETE FROM {table}")
    conn.commit()
    conn.close()

def test_generatePassword():
    friendly = 'calliope'
    user_type = 1
    password = 'callie'

    connection_start('USERS')
    passFunctions.generatePassword(user_type, friendly, password)
    conn = sqlite3.connect(db)
    out = conn.execute(f'SELECT key, salt FROM USERS WHERE friendly="{friendly}"')
    for row in out:
        key = row[0]
        salt = row[1]
    assert key is not None
    assert salt is not None

    conn.execute("DELETE FROM USERS")
    conn.commit()
    conn.close()


def test_verifyPassword():
    friendly = 'calliope'
    user_type = 1
    password = 'callie'

    conn = sqlite3.connect(db)
    conn.execute("DELETE FROM USERS")
    conn.commit()
    conn.close()

    passFunctions.generatePassword(user_type, friendly, password)
    check = passFunctions.verifyPassword(friendly, password)

    assert check == True

    check = passFunctions.verifyPassword(friendly, 'deadbeef')
     
    assert check == False
    
    conn = sqlite3.connect(db)
    conn.execute("DELETE FROM USERS")
    conn.commit()
    conn.close()

    # don't forget to check the hex