import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27610729"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dc8baf2c428bff04c5350c89cbbd842f")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://leader:@wael2005#@cluster0.4vcwctj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
