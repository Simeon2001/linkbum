from django.urls import path
from . import views

urlpatterns = [
    path('info/<str:uname>', views.libum, name = 'linkers/' ),
]