import pytz, json, jwt
from datetime import datetime, timezone
import time
from Backend.Database.connect import client
from dotenv import dotenv_values
config = dotenv_values(".env")
def get_token(request):
    token = request.headers['Authorization']
    token = token.replace('Bearer ', '')
    return token
