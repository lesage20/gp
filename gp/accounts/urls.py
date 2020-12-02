from django.urls import path
from django.contrib.auth import views as auth_view


from . import views

urlpatterns = [

    path('register',views.registerUser, name='register'),
    path('login',views.loginUser, name='login'),
    path('logout',views.logoutUser, name='logout'),
    path('user',views.userPage, name='user'),
    path('user-settings',views.Usettings, name='user-settings'),
    
   
]