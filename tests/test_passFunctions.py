import SOARback.passFunctions as passFunctions
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

def test_generatePassword(mocker):
    user_type = 1
    friendly = 'help'
    connection_start('USERS')
    mocker.patch('SOARback.passFunctions.getRFIDData', return_value=['help', 'me'])
    passFunctions.generatePassword(user_type)
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


def test_verifyPassword(mocker):
    friendly = 'calliope'
    user_type = 1
    password = 'callie'

    connection_start('USERS')

    mocker.patch('SOARback.passFunctions.getRFIDData', return_value=['help', 'me'])
    passFunctions.generatePassword(1)
    mocker.patch('SOARback.passFunctions.getRFIDData', return_value=['help', 'me2'])
    passFunctions.generatePassword(2)
    mocker.patch('SOARback.passFunctions.getRFIDData', return_value=[friendly, password])
    passFunctions.generatePassword(user_type)

    mocker.patch('SOARback.passFunctions.getRFIDData', return_value=[friendly, password])
    check = passFunctions.verifyPassword()
    assert check == True

    mocker.patch('SOARback.passFunctions.getRFIDData', return_value=[friendly, 'me'])
    check = passFunctions.verifyPassword()
    assert check == False
    
    connection_start('USERS')

def test_getUserPermissions(mocker):
    friendly = 'calliope'
    user_type = 2
    password = 'callie'

    connection_start('USERS')
    mocker.patch('SOARback.passFunctions.getRFIDData', return_value=[friendly, password])
    passFunctions.generatePassword(user_type)

    view, edit = passFunctions.getUserPermissions(friendly)

    assert view == 0
    assert edit == 1

    conn = sqlite3.connect(db)
    conn.execute("DELETE FROM USERS")
    conn.commit()
    conn.close()