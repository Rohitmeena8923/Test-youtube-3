# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27775431"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "b70bb1d45a1d05236671d4cc615e40f9")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8178852587:AAHJZKUTfmE-m78xrlmH9VvD9RUw1VXEU00")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Rohittube321bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6414266397"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6414266397").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-2446676469"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Rohitmeena64:Ajmeer234590577@cluster0.mae8oyn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-2446676469"))

