from django.shortcuts import redirect
from rest_framework import generics
from .serializers import profile_create,social_serializer,UserSerializer
from .models import profile,Social_Media,site_links
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User 
from rest_framework	import status
from django.contrib.auth import get_user_model 
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from django.contrib.auth import login, authenticate
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

@login_required 
@api_view(['get'])
def profilex (request):   
    the_user = profile.objects.filter(Q(user=request.user))
    serializer_class = profile_create(the_user, many=True)
    return Response(serializer_class.data)

# social media view vccgg

@login_required 
@api_view(['get'])
def soclink (request):
    if request.method == 'GET':
        b = request.user
        pro_orm = profile.objects.get(user=b)
        c = Social_Media.objects.get(user=pro_orm)
    
        serializer_class = social_serializer(c)
        return Response(serializer_class.data)

# social media link post request
@api_view(['post'])
def post_soclink (request):
    if	request.method	==	'POST':
        b = request.user
        fbk = request.data.get("fbk")
        twr = request.data.get("twr")
        ins = request.data.get("ins")
        whp = request.data.get("whp")
        snt = request.data.get("snt")
        gtb = request.data.get("gtb")
        pro_orm,created = profile.objects.get_or_create(user=b)
        c,created = Social_Media.objects.get_or_create(user=pro_orm)
        c.fbk = fbk
        c.twr = twr
        c.ins = ins
        c.whp = whp
        c.snt = snt
        c.gtb = gtb
        c.save()
        serializer_class = social_serializer(c)
        return Response(serializer_class.data)
    else:
        return Response (serializer_class.errors, status=status.HTTP_401_BAD_REQUEST)

 
# POST LINK VIEW
@login_required
@api_view(['post'])
def post_libum (request):
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

@api_view(['GET','POST'])
def register(request):
    if request.method == "POST":
        #Getting the data of the user
        username = request.data.get("username")
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")
        pics = request.data.get("pics")
        info = request.data.get("info")
        check_user = User.objects.filter(Q(username=username))
        if check_user.exists():
            return Response({"That username is taken"})
        else:
            user = User.objects.create(username=username, password = password, email=email)
            user.set_password(password)
            user.save()
            log_user_in = authenticate(username=username, password=password)
            login(request, log_user_in)
            #Getting the new user id to attach it to his/her profile
            check_stuff = User.objects.get(username=username)
            profile.objects.create(user=check_stuff, pics=pics, info=info)
            return redirect("/api/profile")
    else:
        return Response({"Page":"Registration Page"})

class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [JSONParser]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
