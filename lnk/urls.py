from django.urls import path
from lnk import views
from lnk.views import LoginAPI

urlpatterns = [
    path ('api/profile', views.profilex, name = 'Home/' ),
    path ('accounts/login/', LoginAPI.as_view(), name = 'login/' ),
    path('api/slink', views.soclink, name = 'slink/' ),
    path('api/slink/create', views.post_soclink, name='soclink_create/'),
    path('api/register', views.register, name = 'register/' ),
    path('api/links', views.post_libum, name = 'linkers/' ),
    #path('<int:pk>/feedback', views.fed, name = 'feed/' ),
]