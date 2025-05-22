import os

APP_NAME = "MyLoginApp"
APPDATA_FOLDER = os.path.join(os.getenv("APPDATA"), APP_NAME)
os.makedirs(APPDATA_FOLDER, exist_ok=True)

ACCOUNTS_FILE = os.path.join(APPDATA_FOLDER, "accounts.json")
