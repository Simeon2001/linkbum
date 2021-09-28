from rest_framework import serializers
from lnk.models import profile,Social_Media,site_links,feedback
from lnk.serializers import social_serializer

class siteserial (serializers.HyperlinkedModelSerializer):
    users = social_serializer()
    

    class Meta:
        model = site_links
        fields = ['id', 'url_link', 'details', 'clicks','users']