from django.urls import path
from . import views

urlpatterns = [
#    path('mapping/', views.mapcolumns),
#    path('', views.simple_upload),
#     path('fieldmapping', views.fieldmatching),
     path('import', views.import_data),
     path('fieldmatching', views.fieldmatching),
#     path('impart', views.impart_data),
#     path('fieldmathing', views.fieldmathing)
    ]
