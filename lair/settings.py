import os

TWITTER = {  # You need to set up twitter API keys in settings_loca.py
    "consumer_key": None,
    "consumer_secret": None,
    "token": None,
    "token_secret": None,
}

MONGO_CONNECTION = {}
MONGO_DB = 'lair'

TESTING = os.environ.get('TESTING', '')

if TESTING:
    MONGO_DB = 'lair_test'

try:
    from settings_local import *
except ImportError:
    pass
