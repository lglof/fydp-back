import os
import hashlib
import sys
import sqlite3
from definitions import ROOT_DIR

db = os.path.join(ROOT_DIR, 'SOARback/db/SOARback_users.db')
usersTable = 'USERS'
typesTable = 'USER_TYPES'

def generatePassword(user_type, friendly, password):
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

def verifyPassword(friendly, password):
    conn = sqlite3.connect(db)
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

# def getUserType():
