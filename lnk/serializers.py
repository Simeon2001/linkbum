from rest_framework import serializers
from .models import profile,Social_Media,site_links,feedback

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
    
    class Meta:
        model = profile
        fields = ['id', 'user', 'pics', 'info','name']

class social_serializer (serializers.ModelSerializer):
    user = profile_create()

    class Meta:
        model = Social_Media
        fields = ['user', 'fbk', 'twr', 'ins','whp','snt','gtb']


