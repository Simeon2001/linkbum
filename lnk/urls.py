from django.urls import path
from lnk import views
from lnk.views import UserCreateView


urlpatterns = [
    path ('api/profile', views.profilex, name = 'Home/' ),
    path ('api/procreate', views.post_profilex, name = 'Home/' ),
    path('api/slink', views.soclink, name = 'slink/' ),
    path('api/slink/create', views.post_soclink, name='soclink_create/'),
    path('api/register', UserCreateView.as_view(), name = 'register/' ),
    path('api/links', views.post_libum, name = 'linkers/' ),
    #path('<int:pk>/feedback', views.fed, name = 'feed/' ),
]