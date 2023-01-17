import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5832833379:AAFz-EPc0uJ8GXJDTjtMU0g3CHptGru5Ek4")

APP_ID = int(os.environ.get("APP_ID", "13355224"))

API_HASH = os.environ.get("API_HASH", "48394ec896a45728122d085f7d3d9c20")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001625103853"))

OWNER_ID = int(os.environ.get("OWNER_ID", "1673474401"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get("START_MESSAGE", "Hello {firstname}!\n\nI am a File Sharing Bot made by @CodeXBotz")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
