from django.urls import path
from . import views

urlpatterns = [
    path('<str:uname>', views.libum, name = 'linkers/' ),
]