from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 4327214
    API_HASH = "a926431026a94d0885a735cddaef4ac1"
    # the name to display in your alive message
    ALIVE_NAME = "BOTTO"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://athena:athena@catuserbot.joq3u9k.mongodb.net/?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOL4Bu1RD6_ygij5-9PbZDi-hzDGCvO-aZfeuahKDblAI5RD4IZUgNJnEPt6HBIQZuoF01PBu7_fA1XJtIpDkF1Le90_7Etb9Oacl6K5ywO1e-l6y6G5l3AUIfUNUU4842zCc_PajD-s9_flRjQuN7-9zkAr7oHeiQ1gLJmVUiaKtapUSxJasTEjp5z-RIs9uDtv_XA9A4tVYRXR2yHUDlH0gZ0uIDY2ZZAUGvDV7_Hi8slxo2C85hmkWzbB22yvTE-Zn2LW5bsF6P8YSwBM7keoaEPQ5AKUtvvX3lLnNC1fyebjLc7tD3fpYwmuuGTbBRPdNjSd5KqJe32bov-4uvzn8p4A="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "1711446089:AAFfQOdXgLVBkAHKl4cNOqygvdi8wCBkHlk"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -823912393
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"