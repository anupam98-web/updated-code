from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.home, name='index'),
    path('blank', views.blank_dash),
    path('buttons', views.buttons_dash),
    path('cards', views.cards_dash),
    path('charts', views.charts_dash),
    path('forgot-password', views.forgot_password),
    path('404', views.error_404),
    path('login_dash', views.login_dash),
    path('tables', views.tables_dash),
    path('utilities-animation', views.utilities_animation),
    path('utilities-border', views.utilities_border),
    path('utilities-color', views.utilities_color),
    path('utilities-other', views.utilities_other),
    path('register', views.register),
    path('choose', views.upload),

]
