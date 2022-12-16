from pymongo import MongoClient
import urllib.parse
from dotenv import dotenv_values
# Create your views here.
config = dotenv_values(".env")

try:
    db_usn = urllib.parse.quote_plus(config.get('DB_USERNAME'))
    db_pwd = urllib.parse.quote_plus(config.get('DB_PASSWORD'))
    connection_string = f"mongodb+srv://{db_usn}:{db_pwd}@cluster0.pfauaz8.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_string, connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1)
    print(client)
except Exception as E:
    print(E)

