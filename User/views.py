from django.shortcuts import render
from rest_framework.decorators import APIView,api_view
from .models import UsersDetails
from rest_framework.response import Response
from .serializers import UsersSerializer
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_202_ACCEPTED,HTTP_304_NOT_MODIFIED



# Create your views here.

class users(APIView):

    def get(self,request):
        users_data = UsersDetails.objects.all()
        users = UsersSerializer(users_data, many = True)
        return Response(users.data, status = HTTP_200_OK)
    
    def post(self,request):
        userData = UsersSerializer(data = request.data)
        print(userData)
        if userData.is_valid():
            userData.save()
            users = UsersDetails.objects.all()
            users = UsersSerializer(users,many=True)
            return Response(users.data,status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)

   
@api_view(['GET','PUT','DELETE'])
def Modify(request,name):
    
    try:
        user = UsersDetails.objects.get(User_Name = name)
    
    except UsersDetails.DoesNotExist:
        return Response({'Error': 'User does not exist'}, status=HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        user = UsersSerializer(user)
        return Response(user.data,status=HTTP_200_OK)
    
    if request.method == 'PUT':
        userData = UsersSerializer(user, data = request.data)
        if userData.is_valid():
            userData.save()
            return Response(status=HTTP_202_ACCEPTED)
        return Response(userData,status=HTTP_304_NOT_MODIFIED)

    if request.method == 'DELETE':
        user.delete()
        users = UsersDetails.objects.all()
        users = UsersSerializer(users, many = True)
        return Response(users.data, status=HTTP_202_ACCEPTED)