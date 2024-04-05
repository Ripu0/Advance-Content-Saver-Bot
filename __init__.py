#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("29512038", default=None, cast=int)
API_HASH = config("abf6061a0c9c8c30cecf9f1e4d6a84cc", default=None)
BOT_TOKEN = config("6599241917:AAEuXmqZAwhr_ZecUwG_Mk1xBqVLAZfR7Ho", default=None)
SESSION = config("BQAe9LQYF8UR8OU697xfY3-15LglUAVqHX_cheeyQTjmY-IyRRGKen4CEbLcl3-CrwOrZslE8v8QJzG8ZDRJ9eFZH3yn-kHNKM8bNxXvdtJYgJ294euAYVJDrwt3ZdwZexEzrJgw-lJlGdGmDlEgepAeMi8MLCs-YXnZ1zYqI0J5q6UYLLauqwHGv8BxbkgbARawY1wVGHNHwhwBD0m2e_1Yqc3lYRCrho1SECZxg6sPyfRJtEH1w5gcHl3lrPnf6SeHXJzcprX0VHzYASNRgJEKSXC3JHnL1WXMHzayK20bNbosSfGnitDgqJl5dEY3gYRgEYrKTQ9F3tTurala9WMtAAAAASqVMeoA", default=None)
FORCESUB = config("IM Forwarder", default=None)
AUTH = config("5009388010", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
