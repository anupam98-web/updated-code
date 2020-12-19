from django.urls import path
from mapping import views

urlpatterns = [
        path('import', views.import_data),
        path('fieldmatching', views.fieldmatching),
        path('choose', views.choose),
        path('import_p', views.import_data_p),
        path('mandate_import', views.mandate_import_data),
        path('mandate_fieldmatching', views.mandate_fieldmatching),
        path('mandate_choose', views.mandate_choose),
        path('mandate_import_p', views.mandate_import_data_p),
        path('datavisual', views.visualization),

]
