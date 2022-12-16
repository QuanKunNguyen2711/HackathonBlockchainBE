from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Backend.Database.connect import client
from Backend.Common.utils import get_token
import json
import gridfs
from dotenv import dotenv_values
from threading import Thread

config = dotenv_values(".env")

@api_view(["POST"])
def post_project(request):
    near_address = get_token(request)
    if near_address is None:
        return Response('Invalid token', status=status.HTTP_400_BAD_REQUEST)
    project_data = request.data
    db = getattr(client, 'HackathonBlockchain')
    try:
        search_project = db['Projects'].find_one({
            '_id': str(project_data.get('jobsId'))
        })
        if search_project is None:
            project_data['_id'] = str(project_data.get('jobsId'))
            del project_data['jobsId']
            fs = gridfs.GridFS(db)
            uid = fs.put(project_data.get('document').encode('ascii'))
            project_data['document'] = uid
            project_data['active'] = True
            project_data['post_by'] = near_address
            db['Projects'].insert_one(project_data) # Create new default user's object in database
            return Response("Post successfully", status=status.HTTP_201_CREATED)
        return Response(json.dumps(search_project), status=status.HTTP_200_OK)
    except Exception as E:
        print(E)
        return Response(E, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def get_detail(request):
    near_address = get_token(request)
    if near_address is None:
        return Response('Invalid token', status=status.HTTP_400_BAD_REQUEST)
    jobId = request.data.get('jobId')
    db = getattr(client, 'HackathonBlockchain')
    try:
        search_project = db['Projects'].find_one({
            '_id': str(jobId),
            'active': True
        })
        if search_project is not None:
            fs = gridfs.GridFS(db)
            bytes_file = fs.get(search_project['document']).read()
            del search_project['document']
            search_project['document'] = bytes_file
            return Response(search_project, status=status.HTTP_200_OK)
        return Response("Not found", status=status.HTTP_400_BAD_REQUEST)
    except Exception as E:
        print(E)
        return Response(E, status=status.HTTP_400_BAD_REQUEST)

res_projects = []
def get_file(db, project):
    fs = gridfs.GridFS(db)
    bytes_file = fs.get(project['document']).read()
    del project['document']
    project['document'] = str(bytes_file.decode('ascii'))
    global res_projects
    res_projects.append(project)
@api_view(["GET"])
def list_projects(request):
    near_address = get_token(request)
    if near_address is None:
        return Response('Invalid token', status=status.HTTP_400_BAD_REQUEST)
    db = getattr(client, 'HackathonBlockchain')
    try:
        list_projects = list(db['Projects'].find({
            'active': True
        }))
        threads = [Thread(target=get_file, args=(db, project)) for project in list_projects]
        [t.start() for t in threads]
        [t.join() for t in threads]

        return Response(res_projects, status=status.HTTP_200_OK)
    except Exception as E:
        print(E)
        return Response(E, status=status.HTTP_400_BAD_REQUEST)
