   
from rest_framework.response import Response

def api_success_response(data,message="Success",code=200,headers=None):
    return Response({
        "status": code,
        "message": message,
        "data": data
    }, code, headers=headers)

def api_error_response(error,message="Error",code=422,headers=None):
    return Response({
        "status": code,
        "message": message,
        "error": error
    }, code, headers=headers)