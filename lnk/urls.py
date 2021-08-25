from django.urls import path
from lnk import views

urlpatterns = [
    path ('lt/profile', views.profilex, name = 'Home/' ),
    path ('lt/procreate', views.post_profilex, name = 'Home/' ),
    path('lt/slink', views.soclink, name = 'slink/' ),
    path('slink/create', views.post_soclink, name='soclink_create/'),
    #path('<str:uname>', views.libum, name = 'linkers/' ),
    path('lt/links', views.post_libum, name = 'linkers/' ),
    #path('<int:pk>/feedback', views.fed, name = 'feed/' ),
]