from django.urls import path
from lnk import views
from lnk.views import UserCreateView


urlpatterns = [
    path ('lt/profile', views.profilex, name = 'Home/' ),
    path ('lt/procreate', views.post_profilex, name = 'Home/' ),
    path('lt/slink', views.soclink, name = 'slink/' ),
    path('slink/create', views.post_soclink, name='soclink_create/'),
    path('lt/register', UserCreateView.as_view(), name = 'register/' ),
    path('lt/links', views.post_libum, name = 'linkers/' ),
    #path('<int:pk>/feedback', views.fed, name = 'feed/' ),
]