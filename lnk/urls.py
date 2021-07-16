from django.urls import path
from lnk import views

urlpatterns = [
    path ('profile', views.profilex, name = 'Home/' ),
    path('slink', views.soclink, name = 'slink/' ),
    path('<str:uname>', views.libum, name = 'linkers/' ),
    path('<int:pk>/feedback', views.fed, name = 'feed/' ),
]