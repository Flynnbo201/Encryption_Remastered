import os
import sys

import socket

def identify_admin():
    hostname = socket.gethostname()
    adminname = 'Flynn-Gaming-PC'
    if hostname == adminname:
        return True
    else:
        return False
print(identify_admin())




APP_NAME = "MyLoginApp"
APPDATA_FOLDER = os.path.join(os.getenv("APPDATA"), APP_NAME)
os.makedirs(APPDATA_FOLDER, exist_ok=True)

ACCOUNTS_FILE = os.path.join(APPDATA_FOLDER, "accounts.json")
