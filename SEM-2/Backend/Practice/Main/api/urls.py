from django.urls import path
from . import views

urlpatterns = [
    path("",views.getroutes),
    path("room/",views.getrooms),
    path("room/<int:pk>",views.getroomno),
]
