from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path("home/user", user),
    path("index/", index),
    path('registration/', registration,name="registration"),
    path('success/', success, name='success'),
    path('sign-in/',login_view,name="signin"),
   # path('registration/user1', user1),
]
