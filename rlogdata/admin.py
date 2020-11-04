from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rlogdata.models import Staging
import pandas as pd
# Register your models here.

@admin.register(Staging)

class PersonAdmin(ImportExportModelAdmin):
    pass
