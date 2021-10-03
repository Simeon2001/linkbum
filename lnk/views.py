from django.shortcuts import render
from rest_framework import generics
from .serializers import profile_create,social_serializer,UserSerializer
from .models import profile,Social_Media,site_links,feedback
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User 
from rest_framework	import status
from django.contrib.auth import get_user_model 
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication


# Create your views here.

@api_view(['get'])
def profilex (request):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    b = request.user
    t = profile.objects.get(user=b)
    serializer_class = profile_create(t)
    return Response(serializer_class.data)
    

@api_view(['post'])
def post_profilex (request):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    if	request.method	==	'POST':
        user = request.user
        pics = request.data.get("pics")
        info = request.data.get("info")
        create = profile.objects.create(user=user,pics=pics,info=info)
        create.save()
        serializer_class = profile_create(create)
        print (user.id,pics,info)
        return Response (serializer_class.data,status=status.HTTP_201_CREATED)
    else:
        return Response (serializer_class.errors, status=status.HTTP_401_BAD_REQUEST)


# social media view vccgg
@api_view(['get'])
def soclink (request):
    authentication_classes = (TokenAuthentication,)	
    permission_classes = (IsAuthenticated,)
    if	request.method	==	'GET':
        b = request.user
        pro_orm = profile.objects.get(user=b)
        c = Social_Media.objects.get(user=pro_orm)
    
        serializer_class = social_serializer(c)
        return Response(serializer_class.data)

# social media link post request
@api_view(['post'])
def post_soclink (request):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    if	request.method	==	'POST':
        b = request.user
        fbk = request.data.get("fbk")
        twr = request.data.get("twr")
        ins = request.data.get("ins")
        whp = request.data.get("whp")
        snt = request.data.get("snt")
        gtb = request.data.get("gtb")
        pro_orm = profile.objects.get(user=b)
        c = Social_Media.objects.create(user=pro_orm,fbk=fbk,twr=twr,ins=ins,whp=whp,snt=snt,gtb=gtb)
        c.save()
        serializer_class = social_serializer(c)
        return Response(serializer_class.data)
    else:
        return Response (serializer_class.errors, status=status.HTTP_401_BAD_REQUEST)

 
# POST LINK VIEW
@api_view(['post'])
def post_libum (request):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    if	request.method	==	'POST':
        url_link = request.data.get("url")
        details = request.data.get("info")
        name = request.user
        t,created = profile.objects.get_or_create(user=name)
        j,created = Social_Media.objects.get_or_create(user=t)
        x  = site_links.objects.create(users=j,url_link=url_link,details=details)
        x.save()
        return Response(
            {
                "status": True,
                "message": "created",
                "data": request.data
            }
        )

"""
@api_view()
def fed (request,pk):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    n = feedback.objects.filter(user=pk)
    serializer_class = feedserial(n,many=True)
    return Response(serializer_class.data)
"""

class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [JSONParser]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
