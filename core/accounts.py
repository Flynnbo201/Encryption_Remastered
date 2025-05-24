import requests
import json
import time
import hashlib
import os
import requests
from config.paths import ACCOUNTS_FILE

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, provided_password):
    return stored_hash == hash_password(provided_password)

def load_accounts():
    url = "https://drive.google.com/uc?export=download&id=1QplwuPOw8Nx0iMI9eT1yyrYLOlD0zRBB"

    response = requests.get(url)

    try:
        data = response.json()  # parse the JSON content
        return data
    except json.JSONDecodeError:
        print("Failed to decode JSON. Check the file content or permissions.")


def load_accounts_local():
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

