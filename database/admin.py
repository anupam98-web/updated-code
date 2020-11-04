from django.contrib import admin


# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Mandate
@admin.register(Mandate)
class JobAdmin(ImportExportModelAdmin):
    list_display = ('Job_ID', 'Company_Name', 'Job_Category','Job_Sub_Category','HR_Name','Job_Role',
                    'Skills_Required' ,'Creation_Date' ,'End_Date','Number_of_openings' ,'Jopb_Location',
                    'Designation_of_job','ctc','Min_Exp','Max_Exp' ,'CompanyID')

      
