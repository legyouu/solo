import os
from os import getenv
from dotenv import load_dotenv
from OWNER import BOT_TOKEN, OWNER, OWNER_NAME, DATABASE, CHANNEL, GROUP, LOGS, VIDEO

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}



API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
OWNER = getenv("OWNER", "") 
OWNER_NAME = getenv("OWNER_NAME", "") 
CHANNEL = getenv("CHANNEL", "") 
GROUP = getenv("GROUP", "") 
LOGS = getenv("LOGS", "")
VIDEO = getenv("VIDEO", "")