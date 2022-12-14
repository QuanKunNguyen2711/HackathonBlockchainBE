from pymongo import MongoClient
from dotenv import dotenv_values
# Create your views here.

config = dotenv_values(".env")
connection_string = f"mongodb+srv://{config.get('DB_USERNAME')}:{config.get('DB_PASSWORD')}@cluster0.pfauaz8.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)