def get_token(request):
    token = request.headers['Authorization']
    token = token.replace('Bearer ', '')
    return token