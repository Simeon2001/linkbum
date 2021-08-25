from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from lnk.models import profile,site_links
from lnk.serializers import siteserial
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
    x  = site_links.objects.filter(users=t)
    serializer_class = siteserial(x,many=True)
    return Response(serializer_class.data)