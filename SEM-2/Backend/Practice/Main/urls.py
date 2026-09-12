from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path('room/', views.room, name='Rooms'),       
    path('rooms/<int:roomno>/', views.chat, name='Talk'),
    path('create-room/', views.inform, name='Insert'),
    path('update-room/<int:roomno>/', views.upform, name='Update'),
    path('delete-room/<int:roomno>/', views.delform, name='Delete'),
]