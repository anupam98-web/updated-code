from django.urls import path
from login import views

urlpatterns = [
    
    path('',views.login_page),
    path('user_login',views.user_login),
    ]