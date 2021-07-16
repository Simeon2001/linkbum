from django.shortcuts import render
from rest_framework import generics
from .serializers import profile_create,siteserial,social_serializer,feedserial
from .models import profile,Social_Media,site_links,feedback
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User 


# Create your views here.

@api_view(['GET','POST'])
def profilex (request):
    permission_classes = (IsAuthenticated,)
    b = request.user
    t = profile.objects.get(user=b)
    serializer_class = profile_create(t)
    return Response(serializer_class.data)

#social media view vccgg
@api_view()
def soclink (request):
    permission_classes = (IsAuthenticated,)
    b = request.user
    t = profile.objects.get(user=b)
    c = Social_Media.objects.get(user=t)
    
    serializer_class = social_serializer(c)
    return Response(serializer_class.data)

#link view
@api_view(['GET','POST'])
def libum (request,uname):
    permission_classes = (AllowAny,)
    d =  User.objects.get(username=uname) 
    t = profile.objects.get(user=d)
    x  = site_links.objects.filter(users=t)
    serializer_class = siteserial(x,many=True)
    return Response(serializer_class.data)

@api_view()
def fed (request,pk):
    permission_classes = (IsAuthenticated,)
    n = feedback.objects.filter(user=pk)
    serializer_class = feedserial(n,many=True)
    return Response(serializer_class.data)