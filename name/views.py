from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from lnk.models import profile,site_links,Social_Media
from .serializers import siteserial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# Create your views here.
# link view
@login_required 
@api_view()
def libum (request,uname):
    name = User.objects.get(username= uname) 
    t,created = profile.objects.get_or_create(user=name)
    j,created = Social_Media.objects.get_or_create(user=t)
    x  = site_links.objects.filter(users=j)
    serializer_class = siteserial(x,many=True)
    return Response(serializer_class.data)