from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from lnk.models import profile,site_links,Social_Media
from .serializers import siteserial
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# link view
@api_view()
def libum (request,uname):
    permission_classes = (AllowAny,)
    name = User.objects.get(username=uname) 
    t = profile.objects.get(user=name)
    j = Social_Media.objects.get(user=t)
    x  = site_links.objects.filter(users=j)
    serializer_class = siteserial(x,many=True)
    return Response(serializer_class.data)