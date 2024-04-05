from os import environ 

class Config:
    API_ID = environ.get("29512038", "577678")
    API_HASH = environ.get("abf6061a0c9c8c30cecf9f1e4d6a84cc", "d2c6e01uuiuiouioiuiou0fc6d7a1be")
    BOT_TOKEN = environ.get("6599241917:AAEuXmqZAwhr_ZecUwG_Mk1xBqVLAZfR7Ho", "70955...") 
    BOT_SESSION = environ.get("BQHCUWYAaefYA6LJqAEZFYPOJ6VlYMIJ3_cPa-2uFxgAk9q2z_ks3G1j8kKSMuqIqRw8JVGHBwXMid3Frk6QL3aEbr1fVXxcFhENAUGi-7BHGXmHCPl3jbIj9p3SEz0w2MHvQn6EvUcYoir1GI7YLBVF-78vjpnfq08Zs6fSX0lHzF4Yv3At1tmaGZIcdgaea7dQ9_uDOcBH3ydDFvld8fj5WwISKGCIPhWP90n0gH_D-2nH7eJGgZA5LLtrG74PDQm4a0sl7cHa9MZqxv5ZxvuD00bCYG81_OHiFkHwqNFoF1OV5YStsNstbDrcx3O1XuzzM1AG6KFvKT5sl4uwNPu-kEzPVgAAAAGJWHC9AQ", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("5009388010", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
