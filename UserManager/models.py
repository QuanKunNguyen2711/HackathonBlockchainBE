from django.db import models
from bson import ObjectId
import json
# Create your models here.
class User:
    def __init__(self, near,
                 username='',
                 displayName='',
                 contactNumber='',
                 gender='',
                 attachment='',
                 skills=None,
                 image='',
                 address='',
                 state='',
                 zipcode='',
                 country='',
                 overview='',
                 facebook='',
                 linkedIn=''
                 ):
        self._id = str(ObjectId()) # Generate objectID for obj
        self.near_address = near
        self.profile_basic = {
            'username': username,
            'displayName': displayName,
            'contactNumber': contactNumber,
            'gender': gender,
            'attachment': attachment,
            'skills': skills,
            'image': image
        }
        self.location = {
            'address': address,
            'state': state,
            'zipcode': zipcode,
            'country': country
        }
        self.overview = overview
        self.socialLink = {
            'facebook': facebook,
            'linkedIn': linkedIn
        }
# {
#     "near_address": "ed25519:3NqPUHQAcfqMfL93jsVxJPgGFsh4xoa1X1UcLBgZT17N",
#     "profileBasic": {
#         "username": "quan.nguyen2711",
#         "displayName": "Quan Nguyen",
#         "contactNumber": "0857915202",
#         "gender": "Male",
#         "attachment": "<link>",
#         "skills": [
#             "Rust",
#             "Python",
#             "Nodejs",
#             "React"
#         ],
#         "image": "<base64:image>"
#     },
#     "location": {
#         "address": "67 Mai Chi Tho",
#         "state": "district 2",
#         "zipcode": "71106",
#         "country": "Viet Nam"
#     },
#     "overview": "Tui là Quân, bla bla",
#     "socialLink": {
#         "facebook": "<link>",
#         "linkedIn": "<link>"
#     }
# }