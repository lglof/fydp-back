import os
import hashlib
import sys
from definitions import ROOT_DIR

passFile = os.path.join(ROOT_DIR, 'pass.txt')

def generatePassword(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )

    out = salt + key
    open(passFile, 'w+').close()
    with open(passFile, "wb") as passwordFile:
        passwordFile.write(out)
    return 1

# both pass and key are 32 bytes
def verify(passwordToCheck):
    with open(passFile, 'rb') as passfile:
        salt = passfile.read(32)
        key = passfile.read(32)

    HpasswordToCheck = hashlib.pbkdf2_hmac(
        'sha256',
        passwordToCheck.encode('utf-8'),
        salt, 
        100000
    )

    if HpasswordToCheck == key:
        return True
    else:
        return False


