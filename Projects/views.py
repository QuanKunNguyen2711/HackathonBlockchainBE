from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Backend.Database.connect import client
from Backend.Common.utils import get_token
from UserManager.models import User
from bson import ObjectId
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

@api_view(["POST"])
def post_project(request):
    near_address = get_token(request)
    project_data = request.data
    db = getattr(client, 'HackathonBlockchain')
    try:
        find_user = db['Users'].find_one({
            'near_address': near_address
        })
        if find_user is None: # New user login by near wallet
            newUser = User(near=near_address).__dict__
            db['Users'].insert_one(newUser) # Create new default user's object in database
            return Response(newUser, status=status.HTTP_200_OK)
        return Response(find_user, status=status.HTTP_200_OK)
    except Exception as E:
        print(E)
        return Response(E, status=status.HTTP_400_BAD_REQUEST)