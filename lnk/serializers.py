from rest_framework import serializers
from .models import profile,Social_Media,site_links,feedback
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

class feedserial (serializers.HyperlinkedModelSerializer):

    class Meta:
        model = feedback
        fields = ['id','msg']

class siteserial (serializers.HyperlinkedModelSerializer):
    feeds = feedserial(many=True)
    

    class Meta:
        model = site_links
        fields = ['id', 'url_link', 'details', 'clicks','feeds']
        


#profile serializers
class profile_create (serializers.ModelSerializer):
    name = siteserial(many=True)
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = profile
        fields = ['id', 'user', 'pics', 'info','name']

class social_serializer (serializers.ModelSerializer):
    user = profile_create()

    class Meta:
        model = Social_Media
        fields = ['user', 'fbk', 'twr', 'ins','whp','snt','gtb']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = UserModel.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        new_token = Token.objects.create(user=user)
        return user

    class Meta:
        model = get_user_model()
        fields = [ "username", "password"]
