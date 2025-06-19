from django.shortcuts import render
from rest_framework.decorators import api_view  ,permission_classes
# Create your views here.
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])

def registration_view(req):

    if req.method=='POST':
        serializer=UserRegistrationSerializer(data=req.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='Registration Sucesssfull !!!!'
            data['username']=account.username
            data['email']=account.email
            refresh=RefreshToken.for_user(account)
            data['token']={
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            }

        else:
            data=serializer.errors

        return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response({"details":"Logout succesfull"},status=status.HTTP_200_OK)
