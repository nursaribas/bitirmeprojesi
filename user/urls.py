from django import views
from django.urls import path
from . import views


 #html sayfalarının url sinin belirlenmesi
urlpatterns = [
   path('', views.index , name ='index'),
   path('menu/profile/', views.profile, name ='profile'),
   path('login/', views.login, name="login"),
   path('logout/', views.logout, name="logout"),
   path('register/', views.register, name="register"),
   path('email/',views.email, name='email'),
   
]