import os
import hashlib
import sys
import sqlite3

from definitions import ROOT_DIR
from SOARback.rfidFunctions import getRFIDData

db = os.path.join(ROOT_DIR, 'SOARback/db/SOARback_users.db')
usersTable = 'USERS'
typesTable = 'USER_TYPES'

def generatePassword(user_type):
    rfidData = getRFIDData()
    friendly = rfidData[0]
    password = rfidData[1]
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    conn = sqlite3.connect(db)
    query = (f'INSERT INTO {usersTable} '
        + f'(friendly, salt, key, user_type)'
        + f' VALUES ("{friendly}", "{salt.hex()}", "{key.hex()}", "{user_type}")')
    conn.execute(query)
    conn.commit()
    conn.close()
    return 1

def verifyPassword():
    conn = sqlite3.connect(db)
    rfidData = getRFIDData()
    friendly = rfidData[0]
    password = rfidData[1]
    out = conn.execute(f'SELECT key, salt from USERS where friendly="{friendly}"')
    for row in out: 
        realKey = row[0]
        salt = row[1]
    salt = bytes.fromhex(salt)
    keyToCheck = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    ).hex()
    if keyToCheck == realKey:
        return True
    else:
        return False

def getUserPermissions(friendly):
    query = (f'SELECT USER_TYPES.edit, USER_TYPES.view '
        + f'FROM USERS JOIN USER_TYPES ON USERS.user_type=USER_TYPES.id '
        + f'WHERE USERS.friendly="{friendly}"')

    conn = sqlite3.connect(db)
    out = conn.execute(query)
    for row in out:
        edit = row[0]
        view = row[1]
    return view, edit
