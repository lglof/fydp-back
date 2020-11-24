from SOARback import passFunctions
import os
from definitions import ROOT_DIR

passFile = os.path.join(ROOT_DIR, 'pass.txt')

def test_initSecurity_new_password():
    open(passFile, 'w+').close()
    passFunctions.generatePassword('1234')
    assert passFunctions.verify('1234') == True