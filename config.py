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
BOT_TOKEN = getenv("BOT_TOKEN", "6013587287:AAHQPzV9AjHaNFBMQbB-yYncRARIvAE0dhw")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://bot_vambir:Al2552001@cluster0.heabj.mongodb.net/vambir_bot?retryWrites=true&w=majority)
OWNER = getenv("OWNER", "1236115319") 
OWNER_NAME = getenv("OWNER_NAME", "L120N") 
CHANNEL = getenv("CHANNEL", "UU_Le2") 
GROUP = getenv("GROUP", "L109N") 
LOGS = getenv("LOGS", "L109N")
VIDEO = getenv("VIDEO", "https://t.me/UU_Le2)
