import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 27477919))

    API_HASH = os.environ.get("API_HASH", "b25cce1727f6d33d41d9e00e3ed62583")
