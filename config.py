import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27610729"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dc8baf2c428bff04c5350c89cbbd842f")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://dzfrench84:<gi0dOJMBsk3C24zf>@cluster0.zbpvdt2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
