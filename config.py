from os import environ 

class Config:
    API_ID = environ.get("29512038", "577678")
    API_HASH = environ.get("abf6061a0c9c8c30cecf9f1e4d6a84cc", "d2c6e01uuiuiouioiuiou0fc6d7a1be")
    BOT_TOKEN = environ.get("7061820565:AAEuvZNUyjLmjoY5A5LczaNsYgJQgwCtvK0", "70955...") 
    BOT_SESSION = environ.get("BQHCUWYAangefdqkw3EeojRXfYlXxzqO3dnBskcNvTWwvKkSKsP5o1H2ZDY30ZhJxWou-1jPseiNkL5ou-uHd5DVX6Sz_hjpBr3IJohrqjSrXLhFY4eK4okIR5HBf6PwS-XFUYIWCxt7uJhqKq3Nqiv7Fi5l-JfaFGeq5GvtBHLa-GMSIneHiUTiEhL9qX1vclXjGpl7etUKwE6JdesZdhFi7hrrwx2JT9WlMel2Y62DuRs2LHN_aZwRZ_m-1ABF4CtUHCcEhkl2PTN-TEBMCh2hdZQ0liiSUnnlnAqGw_mkPLvuhXs4LudYoVCio8AZ_47Xn6okR8Z0PI-9uFocYp9n0oG6YAAAAAEqlTHqAA", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("5009388010", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
