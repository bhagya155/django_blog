from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('loginview',views.loginview,name='loginview'),
    path('handlelogout',views.handlelogout,name='handlelogout'),
    path('register',views.register,name='register'),
    path('user',views.user,name='user'),
    path('patient',views.patient,name='patient'),
]