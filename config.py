from os import environ 

class Config:
    API_ID = environ.get("29512038", "577678")
    API_HASH = environ.get("abf6061a0c9c8c30cecf9f1e4d6a84cc", "d2c6e01uuiuiouioiuiou0fc6d7a1be")
    BOT_TOKEN = environ.get("7061820565:AAEuvZNUyjLmjoY5A5LczaNsYgJQgwCtvK0", "70955...") 
    BOT_SESSION = environ.get("BQHCUWYALycsPPnonz84uUuZcNbxexy3PNOWZIMIgmtoPY1BsrnbKnDNzkGB7wsO1gSILPq46vLy-KcYidIX8XhgupwyJDEcaOc5dp7oAHSYP1OcVEFYzSiCbwtCFiXN5Rb39X_aGFJpW9RVGwK8wDT9nJ7AY6DdQYxAzbI9kvEE_ATehoaBGw8jScDcPD3d4p4EFNesMWckE2H4b1wfE2EAU7J4BNO7Tz6DwZxTB2-HD-EmvtjuwbmTPlksGgKY3DRobDi09bYynypGclsD5_FT5TkPB-JsHV6oFAP7a3t83gpXBEHnAqLbe-53kcfF8pRAJ8VwJ4mlr8oETA7Z5i3ZO-g2kAAAAAGk6tSVAQ", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("5009388010", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
