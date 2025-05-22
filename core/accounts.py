import json
import time
import hashlib
import os
from config.paths import ACCOUNTS_FILE

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, provided_password):
    return stored_hash == hash_password(provided_password)

def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as f:
            return json.load(f)
    else:
        with open(ACCOUNTS_FILE, "w") as f:
            json.dump({}, f, indent=4)
        time.sleep(1)
        with open(ACCOUNTS_FILE, 'r') as f:
            return json.load(f)

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)
