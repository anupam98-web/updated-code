from django.db import models


# Create your models here.
class Mandate(models.Model):
        Job_ID = models.CharField(max_length=50)
        Company_Name = models.TextField(max_length=200)
        Job_Category= models.CharField(max_length= 100)
        Job_Sub_Category =models.CharField(max_length = 100, default='')
        HR_Name = models.TextField(max_length=100)
        Job_Role = models.CharField(max_length=3000, default='')
        Skills_Required = models.CharField(max_length=3000,default='', null=True)
        Creation_Date = models.DateField()
        End_Date = models.DateField(default='')
        Number_of_openings = models.IntegerField()
        Jopb_Location = models.CharField(max_length = 300)
        Designation_of_job = models.CharField(max_length=200, blank=True, null=True)
        ctc = models.IntegerField()
        Min_Exp = models.IntegerField()
        Max_Exp = models.IntegerField()
        CompanyID = models.CharField(max_length = 50)

        def savedata(self):
		        self.save()

class Pipeline(models.Model):

            Recruiter = models.CharField(max_length=100,null=True)
            Client = models.CharField(max_length=150,null=True)
            Position = models.CharField(max_length=100,null=True)
            Recruiter_date = models.DateField(null=True)
            CV_sub_date = models.DateField(null=True)
            Candidate_name = models.CharField(max_length=50, null=True)
            Current_status_no = models.IntegerField(null=True)
            Current_status_descr = models.CharField(max_length=30,null=True)
            Interview_date = models.DateField(null=True)
            Remarks = models.TextField(null=True)
            Profile_skills = models.TextField(null=True)
            Current_org = models.TextField(null=True)
            Qualification = models.CharField(max_length=30,null=True)
            Experience = models.IntegerField(null=True)
            Current_Loc = models.CharField(max_length=30,null=True)
            Contact_no = models.IntegerField(null=True)
            Alternate_contact_no = models.IntegerField(null=True)
            Email_id = models.EmailField(max_length=254,null=True)
            Current_salary = models.IntegerField(null=True)
            Expected_salary = models.IntegerField(null=True)
            Notice_period = models.IntegerField(null=True)
            Offer_date = models.DateField(null=True)
            Offer_amount = models.IntegerField(null=True)
            Joining_date = models.DateField(null=True)
            Vacancy_code = models.IntegerField(null=True)
            Applicant_code = models.IntegerField(null=True)
            Birth_date = models.IntegerField(null=True)
            Birth_month = models.IntegerField(null=True)
            Birth_year = models.IntegerField(null=True)
            Preferred_company = models.TextField(null=True)
            Preferred_Location = models.TextField(null=True)
            Week_no = models.IntegerField(null=True)
            Year = models.IntegerField(null=True)

            def savdata(self):
                        self.save()

