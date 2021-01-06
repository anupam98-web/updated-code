from django.shortcuts import render, redirect
from dashboard import views
from mapping import views
from rlogdata.models import Staging
from mapping.views import visualization
from rlogdata.models import *
import pandas as pd


# Create your views here.

def home(request):
    cred = 'postgresql://postgres:willoffire@1@localhost:5432/Candidate'
    sqldata = pd.read_sql("""
                                SELECT *
                                FROM rlogdata_staging
                                """, con = cred)
        # turn around time
    date_difference = sqldata['date_cv_submitted'] - sqldata['reqt_date']
    y = list(date_difference.dt.days.astype(int))
    counttill2 = 0
    counttill5 = 0
    counttill10 = 0
    countmore = 0
    for i in y:
            if i in range(1,3):
                counttill2 = counttill2 + 1
            if i in range(3, 6):
                counttill5 = counttill5 + 1
            if i in range(6,11):
                counttill10 = counttill10 + 1
            if i in range(11,):
                countmorethan10 = countmore + 1
                
    print(date_difference.dtypes)
        #date_difference.astype(int)
        #print(y)
    print(str(counttill2)+'  '+str(counttill5)+'   '+str(counttill10) + '   ' + str(countmorethan10))
    datecount=0
    for i in y:
            datecount = datecount + i
    #print(datecount)
    TAT = datecount/len(y)
    print('average turn around time',TAT)
    # we have to calculate the no of times i is appearing. 0 to 2, 3 to 5, 6 to 10, 10< above

        # sourcing Effectiveness
    CV_Rejected = Staging.objects.filter(current_status = 102).count()
    Duplicate_CV = Staging.objects.filter(current_status = 101).count()
    Interview_Reject = Staging.objects.filter(current_status__in = [104, 105, 106, 107, 108]).count()
    Interview_Select = Staging.objects.filter(current_status__in = [4, 5, 6, 7, 8]).count()
    CV_Shortlisted = Staging.objects.filter(current_status =  2).count()
        # sourcing effectiveness ends

        # Candidate quality index
    Offered = Staging.objects.filter(current_status = 10).count()
    HR_Rejects = Staging.objects.filter(current_status = 108).count()
        # interview reject same as above
        # interview select samw as above

        # Candidate quality index ends

        # Candidate Intimacy
    Joined = Staging.objects.filter(current_status = 14).count()
    Rejected = Staging.objects.filter(current_status__in = [102, 103, 104, 105, 106,107,108]).count()
    Accepted = Staging.objects.filter(current_status = 11).count()
    
        #  offered same as above

        # end of candidate intimacy

    table = Staging.objects.only('candidate_name', 'client', 'contact_details_mobile', 'joining_date')[:10]
    return render(request, 'index_dash.html', {'TAT_categories': ['0-2','3-5','6-10','10 above'],
                                           'TAT_categories_value':[counttill2, counttill5, counttill10, countmorethan10],
                                           'sourcing_Effectiveness':['CV_Rejected', 'Duplicate_CV', 'Interview_Reject', 'Interview_Select', 'CV_Shortlisted'],
                                           'sourcing_Effectiveness_values': [CV_Rejected, Duplicate_CV, Interview_Reject, Interview_Select, CV_Shortlisted],
                                           'Candidate_quality_index': ['Offered', 'HR_Rejects', 'Interview_Reject', 'Interview_Select'],
                                           'Candidate_quality_index_val': [Offered, HR_Rejects, Interview_Reject, Interview_Select],
                                           'Candidate_Intimacy': ['Joined', 'Rejected', 'Accepted', 'Offered'],
                                           'Candidate_Intimacy_value': [Joined, Rejected, Accepted, Offered],
                                           'table': table}
                  )


def login_dash(request):
    return render(request, 'login_dash.html')


def tables_dash(request):
    table = Staging.objects.all()
    return render(request, 'tables.html', {'table': table})


def utilities_animation(request):
    return render(request, 'utilities-animation.html')


def utilities_border(request):
    return render(request, 'utilities-border.html')


def utilities_color(request):
    return render(request, 'utilities-color.html')


def utilities_other(request):
    return render(request, 'utilities-other.html')


def error_404(request):
    return render(request, '404.html')


def blank_dash(request):
    return render(request, 'blank.html')


def buttons_dash(request):
    return render(request, 'buttons.html')


def cards_dash(request):
    return render(request, 'cards.html')


def charts_dash(request):
    cred = 'postgresql://postgres:willoffire@1@localhost:5432/Candidate'
    sqldata = pd.read_sql("""
                                SELECT *
                                FROM rlogdata_staging
                                """, con = cred)
    # for selection ration of HR
    Hr_int = sqldata[sqldata['current_status']==8]
    print(len(Hr_int.index))
    Hr_rej = sqldata[sqldata['current_status']==108]
    #print(Hr_rej)
    print(len(Hr_rej.index))
    Selection_Ratio_HR = (len(Hr_int.index)-len(Hr_rej.index))/ len(Hr_int.index)
    print("Selection_Ratio_HR: " + str(Selection_Ratio_HR))
    # end selection ration of HR

    # for selection ratio of Tech
    F2F_int = Staging.objects.filter(current_status__in = [5, 6]).count()
    F2F_int_rejects = Staging.objects.filter(current_status__in = [105, 106]).count()
    #print("this is f2f: " + str(F2F_int) + "This is f2f rejects : " + str(F2F_int_rejects))
    F2F_selection_ratio = (F2F_int - F2F_int_rejects)/F2F_int
    print("Selection Ratio Tech: ", F2F_selection_ratio)
    # end selection ration of tech

    # for final interview selection ratio
    Final_int = Staging.objects.filter(current_status = 7).count()
    Final_int_rejects = Staging.objects.filter(current_status = 107).count()
    #print("this is f2f: " + str(F2F_int) + "This is f2f rejects : " + str(F2F_int_rejects))
    Final_selection_ratio = (Final_int - Final_int_rejects)/Final_int
    print("Selection Ratio Final: ", Final_selection_ratio)

    # we use bar graph
    # end selection ratio of final interview
    
    # turn around time
    date_difference = sqldata['date_cv_submitted'] - sqldata['reqt_date']
    y = list(date_difference.dt.days.astype(int))
    counttill2 = 0
    counttill5 = 0
    counttill10 = 0
    countmore = 0
    for i in y:
            if i in range(1,3):
                counttill2 = counttill2 + 1
            if i in range(3, 6):
                counttill5 = counttill5 + 1
            if i in range(6,11):
                counttill10 = counttill10 + 1
            if i in range(11,):
                countmorethan10 = countmore + 1
                
    print(date_difference.dtypes)
        #date_difference.astype(int)
        #print(y)
    print(str(counttill2)+'  '+str(counttill5)+'   '+str(counttill10) + '   ' + str(countmorethan10))
    datecount=0
    for i in y:
            datecount = datecount + i
    #print(datecount)
    TAT = datecount/len(y)
    print('average turn around time',TAT)
    # we have to calculate the no of times i is appearing. 0 to 2, 3 to 5, 6 to 10, 10< above

        # sourcing Effectiveness
    CV_Rejected = Staging.objects.filter(current_status = 102).count()
    Duplicate_CV = Staging.objects.filter(current_status = 101).count()
    Interview_Reject = Staging.objects.filter(current_status__in = [104, 105, 106, 107, 108]).count()
    Interview_Select = Staging.objects.filter(current_status__in = [4, 5, 6, 7, 8]).count()
    CV_Shortlisted = Staging.objects.filter(current_status =  2).count()
        # sourcing effectiveness ends

        # Candidate quality index
    Offered = Staging.objects.filter(current_status = 10).count()
    HR_Rejects = Staging.objects.filter(current_status = 108).count()
        # interview reject same as above
        # interview select samw as above

        # Candidate quality index ends

        # Candidate Intimacy
    Joined = Staging.objects.filter(current_status = 14).count()
    Rejected = Staging.objects.filter(current_status__in = [102, 103, 104, 105, 106,107,108]).count()
    Accepted = Staging.objects.filter(current_status = 11).count()
        #  offered same as above

        # end of candidate intimacy



    
    return render(request, 'charts.html', {'TAT_categories': ['0-2','3-5','6-10','10 above'],
                                           'TAT_categories_value':[counttill2, counttill5, counttill10, countmorethan10],
                                           'Selection_ratio': ['HR','Tech','Final'],
                                           'Selection_ratio_value': [Selection_Ratio_HR, F2F_selection_ratio, Final_selection_ratio],
                                           'sourcing_Effectiveness':['CV_Rejected', 'Duplicate_CV', 'Interview_Reject', 'Interview_Select', 'CV_Shortlisted'],
                                           'sourcing_Effectiveness_values': [CV_Rejected, Duplicate_CV, Interview_Reject, Interview_Select, CV_Shortlisted],
                                           'Candidate_quality_index': ['Offered', 'HR_Rejects', 'Interview_Reject', 'Interview_Select'],
                                           'Candidate_quality_index_val': [Offered, HR_Rejects, Interview_Reject, Interview_Select],
                                           'Candidate_Intimacy': ['Joined', 'Rejected', 'Accepted', 'Offered'],
                                           'Candidate_Intimacy_value': [Joined, Rejected, Accepted, Offered]}
                  )
    #visualization(request)


def forgot_password(request):
    return render(request, 'forgot-password.html')


def register(request):
    return render(request, 'register.html')


def upload(request):
    return redirect('/choose')

def mandate_upload(request):
    return redirect('/mandate_choose')


def badrecords_dash(request):
    return(request,'badrecords_dash.html')


def manageteam_dash(request):
    return(request,'manageteam_dash.html')



def upload_mandate(request):
    return redirect('/mandate_choose')


def display_mandate(request):
    return(request,'display_mandate.html')

def upload_candidate(request):
    return(request,'upload_candidate.html')


def display_candidate(request):
    return(request,'display_candidate.html')


from django.shortcuts import render, redirect
from dashboard import views
from mapping import views
from rlogdata.models import Staging
from mapping.views import visualization
from rlogdata.models import *
import pandas as pd


# Create your views here.

def home(request):
    cred = 'postgresql://postgres:willoffire@1@localhost:5432/Candidate'
    sqldata = pd.read_sql("""
                                SELECT *
                                FROM rlogdata_staging
                                """, con = cred)
        # turn around time
    date_difference = sqldata['date_cv_submitted'] - sqldata['reqt_date']
    y = list(date_difference.dt.days.astype(int))
    counttill2 = 0
    counttill5 = 0
    counttill10 = 0
    countmore = 0
    for i in y:
            if i in range(1,3):
                counttill2 = counttill2 + 1
            if i in range(3, 6):
                counttill5 = counttill5 + 1
            if i in range(6,11):
                counttill10 = counttill10 + 1
            if i in range(11,):
                countmorethan10 = countmore + 1
                
    print(date_difference.dtypes)
        #date_difference.astype(int)
        #print(y)
    print(str(counttill2)+'  '+str(counttill5)+'   '+str(counttill10) + '   ' + str(countmorethan10))
    datecount=0
    for i in y:
            datecount = datecount + i
    #print(datecount)
    TAT = datecount/len(y)
    print('average turn around time',TAT)
    # we have to calculate the no of times i is appearing. 0 to 2, 3 to 5, 6 to 10, 10< above

        # sourcing Effectiveness
    CV_Rejected = Staging.objects.filter(current_status = 102).count()
    Duplicate_CV = Staging.objects.filter(current_status = 101).count()
    Interview_Reject = Staging.objects.filter(current_status__in = [104, 105, 106, 107, 108]).count()
    Interview_Select = Staging.objects.filter(current_status__in = [4, 5, 6, 7, 8]).count()
    CV_Shortlisted = Staging.objects.filter(current_status =  2).count()
        # sourcing effectiveness ends

        # Candidate quality index
    Offered = Staging.objects.filter(current_status = 10).count()
    HR_Rejects = Staging.objects.filter(current_status = 108).count()
        # interview reject same as above
        # interview select samw as above

        # Candidate quality index ends

        # Candidate Intimacy
    Joined = Staging.objects.filter(current_status = 14).count()
    Rejected = Staging.objects.filter(current_status__in = [102, 103, 104, 105, 106,107,108]).count()
    Accepted = Staging.objects.filter(current_status = 11).count()
    
        #  offered same as above

        # end of candidate intimacy

    table = Staging.objects.only('candidate_name', 'client', 'contact_details_mobile', 'joining_date')[:10]
    return render(request, 'index_dash.html', {'TAT_categories': ['0-2','3-5','6-10','10 above'],
                                           'TAT_categories_value':[counttill2, counttill5, counttill10, countmorethan10],
                                           'sourcing_Effectiveness':['CV_Rejected', 'Duplicate_CV', 'Interview_Reject', 'Interview_Select', 'CV_Shortlisted'],
                                           'sourcing_Effectiveness_values': [CV_Rejected, Duplicate_CV, Interview_Reject, Interview_Select, CV_Shortlisted],
                                           'Candidate_quality_index': ['Offered', 'HR_Rejects', 'Interview_Reject', 'Interview_Select'],
                                           'Candidate_quality_index_val': [Offered, HR_Rejects, Interview_Reject, Interview_Select],
                                           'Candidate_Intimacy': ['Joined', 'Rejected', 'Accepted', 'Offered'],
                                           'Candidate_Intimacy_value': [Joined, Rejected, Accepted, Offered],
                                           'table': table}
                  )


def login_dash(request):
    return render(request, 'login_dash.html')


def tables_dash(request):
    table = Staging.objects.all()
    return render(request, 'tables.html', {'table': table})


def utilities_animation(request):
    return render(request, 'utilities-animation.html')


def utilities_border(request):
    return render(request, 'utilities-border.html')


def utilities_color(request):
    return render(request, 'utilities-color.html')


def utilities_other(request):
    return render(request, 'utilities-other.html')


def error_404(request):
    return render(request, '404.html')


def blank_dash(request):
    return render(request, 'blank.html')


def buttons_dash(request):
    return render(request, 'buttons.html')


def cards_dash(request):
    return render(request, 'cards.html')


def charts_dash(request):
    cred = 'postgresql://postgres:willoffire@1@localhost:5432/Candidate'
    sqldata = pd.read_sql("""
                                SELECT *
                                FROM rlogdata_staging
                                """, con = cred)
    # for selection ration of HR
    Hr_int = sqldata[sqldata['current_status']==8]
    print(len(Hr_int.index))
    Hr_rej = sqldata[sqldata['current_status']==108]
    #print(Hr_rej)
    print(len(Hr_rej.index))
    Selection_Ratio_HR = (len(Hr_int.index)-len(Hr_rej.index))/ len(Hr_int.index)
    print("Selection_Ratio_HR: " + str(Selection_Ratio_HR))
    # end selection ration of HR

    # for selection ratio of Tech
    F2F_int = Staging.objects.filter(current_status__in = [5, 6]).count()
    F2F_int_rejects = Staging.objects.filter(current_status__in = [105, 106]).count()
    #print("this is f2f: " + str(F2F_int) + "This is f2f rejects : " + str(F2F_int_rejects))
    F2F_selection_ratio = (F2F_int - F2F_int_rejects)/F2F_int
    print("Selection Ratio Tech: ", F2F_selection_ratio)
    # end selection ration of tech

    # for final interview selection ratio
    Final_int = Staging.objects.filter(current_status = 7).count()
    Final_int_rejects = Staging.objects.filter(current_status = 107).count()
    #print("this is f2f: " + str(F2F_int) + "This is f2f rejects : " + str(F2F_int_rejects))
    Final_selection_ratio = (Final_int - Final_int_rejects)/Final_int
    print("Selection Ratio Final: ", Final_selection_ratio)

    # we use bar graph
    # end selection ratio of final interview
    
    # turn around time
    date_difference = sqldata['date_cv_submitted'] - sqldata['reqt_date']
    y = list(date_difference.dt.days.astype(int))
    counttill2 = 0
    counttill5 = 0
    counttill10 = 0
    countmore = 0
    for i in y:
            if i in range(1,3):
                counttill2 = counttill2 + 1
            if i in range(3, 6):
                counttill5 = counttill5 + 1
            if i in range(6,11):
                counttill10 = counttill10 + 1
            if i in range(11,):
                countmorethan10 = countmore + 1
                
    print(date_difference.dtypes)
        #date_difference.astype(int)
        #print(y)
    print(str(counttill2)+'  '+str(counttill5)+'   '+str(counttill10) + '   ' + str(countmorethan10))
    datecount=0
    for i in y:
            datecount = datecount + i
    #print(datecount)
    TAT = datecount/len(y)
    print('average turn around time',TAT)
    # we have to calculate the no of times i is appearing. 0 to 2, 3 to 5, 6 to 10, 10< above

        # sourcing Effectiveness
    CV_Rejected = Staging.objects.filter(current_status = 102).count()
    Duplicate_CV = Staging.objects.filter(current_status = 101).count()
    Interview_Reject = Staging.objects.filter(current_status__in = [104, 105, 106, 107, 108]).count()
    Interview_Select = Staging.objects.filter(current_status__in = [4, 5, 6, 7, 8]).count()
    CV_Shortlisted = Staging.objects.filter(current_status =  2).count()
        # sourcing effectiveness ends

        # Candidate quality index
    Offered = Staging.objects.filter(current_status = 10).count()
    HR_Rejects = Staging.objects.filter(current_status = 108).count()
        # interview reject same as above
        # interview select samw as above

        # Candidate quality index ends

        # Candidate Intimacy
    Joined = Staging.objects.filter(current_status = 14).count()
    Rejected = Staging.objects.filter(current_status__in = [102, 103, 104, 105, 106,107,108]).count()
    Accepted = Staging.objects.filter(current_status = 11).count()
        #  offered same as above

        # end of candidate intimacy



    
    return render(request, 'charts.html', {'TAT_categories': ['0-2','3-5','6-10','10 above'],
                                           'TAT_categories_value':[counttill2, counttill5, counttill10, countmorethan10],
                                           'Selection_ratio': ['HR','Tech','Final'],
                                           'Selection_ratio_value': [Selection_Ratio_HR, F2F_selection_ratio, Final_selection_ratio],
                                           'sourcing_Effectiveness':['CV_Rejected', 'Duplicate_CV', 'Interview_Reject', 'Interview_Select', 'CV_Shortlisted'],
                                           'sourcing_Effectiveness_values': [CV_Rejected, Duplicate_CV, Interview_Reject, Interview_Select, CV_Shortlisted],
                                           'Candidate_quality_index': ['Offered', 'HR_Rejects', 'Interview_Reject', 'Interview_Select'],
                                           'Candidate_quality_index_val': [Offered, HR_Rejects, Interview_Reject, Interview_Select],
                                           'Candidate_Intimacy': ['Joined', 'Rejected', 'Accepted', 'Offered'],
                                           'Candidate_Intimacy_value': [Joined, Rejected, Accepted, Offered]}
                  )
    #visualization(request)


def forgot_password(request):
    return render(request, 'forgot-password.html')


def register(request):
    return render(request, 'register.html')


def upload(request):
    return redirect('/choose')

def mandate_upload(request):
    return redirect('/mandate_choose')


def badrecords_dash(request):
    return(request,'badrecords_dash.html')


def manageteam_dash(request):
    return(request,'manageteam_dash.html')



def upload_mandate(request):
    return redirect('/mandate_choose')


def display_mandate(request):
    return(request,'display_mandate.html')

def upload_candidate(request):
    return(request,'upload_candidate.html')


def display_candidate(request):
    return(request,'display_candidate.html')


from django.shortcuts import render, redirect
from dashboard import views
from mapping import views
from rlogdata.models import Staging
from mapping.views import visualization
from rlogdata.models import *
import pandas as pd


# Create your views here.

def home(request):
    cred = 'postgresql://postgres:willoffire@1@localhost:5432/Candidate'
    sqldata = pd.read_sql("""
                                SELECT *
                                FROM rlogdata_staging
                                """, con = cred)
        # turn around time
    date_difference = sqldata['date_cv_submitted'] - sqldata['reqt_date']
    y = list(date_difference.dt.days.astype(int))
    counttill2 = 0
    counttill5 = 0
    counttill10 = 0
    countmore = 0
    for i in y:
            if i in range(1,3):
                counttill2 = counttill2 + 1
            if i in range(3, 6):
                counttill5 = counttill5 + 1
            if i in range(6,11):
                counttill10 = counttill10 + 1
            if i in range(11,):
                countmorethan10 = countmore + 1
                
    print(date_difference.dtypes)
        #date_difference.astype(int)
        #print(y)
    print(str(counttill2)+'  '+str(counttill5)+'   '+str(counttill10) + '   ' + str(countmorethan10))
    datecount=0
    for i in y:
            datecount = datecount + i
    #print(datecount)
    TAT = datecount/len(y)
    print('average turn around time',TAT)
    # we have to calculate the no of times i is appearing. 0 to 2, 3 to 5, 6 to 10, 10< above

        # sourcing Effectiveness
    CV_Rejected = Staging.objects.filter(current_status = 102).count()
    Duplicate_CV = Staging.objects.filter(current_status = 101).count()
    Interview_Reject = Staging.objects.filter(current_status__in = [104, 105, 106, 107, 108]).count()
    Interview_Select = Staging.objects.filter(current_status__in = [4, 5, 6, 7, 8]).count()
    CV_Shortlisted = Staging.objects.filter(current_status =  2).count()
        # sourcing effectiveness ends

        # Candidate quality index
    Offered = Staging.objects.filter(current_status = 10).count()
    HR_Rejects = Staging.objects.filter(current_status = 108).count()
        # interview reject same as above
        # interview select samw as above

        # Candidate quality index ends

        # Candidate Intimacy
    Joined = Staging.objects.filter(current_status = 14).count()
    Rejected = Staging.objects.filter(current_status__in = [102, 103, 104, 105, 106,107,108]).count()
    Accepted = Staging.objects.filter(current_status = 11).count()
    
        #  offered same as above

        # end of candidate intimacy

    table = Staging.objects.only('candidate_name', 'client', 'contact_details_mobile', 'joining_date')[:10]
    return render(request, 'index_dash.html', {'TAT_categories': ['0-2','3-5','6-10','10 above'],
                                           'TAT_categories_value':[counttill2, counttill5, counttill10, countmorethan10],
                                           'sourcing_Effectiveness':['CV_Rejected', 'Duplicate_CV', 'Interview_Reject', 'Interview_Select', 'CV_Shortlisted'],
                                           'sourcing_Effectiveness_values': [CV_Rejected, Duplicate_CV, Interview_Reject, Interview_Select, CV_Shortlisted],
                                           'Candidate_quality_index': ['Offered', 'HR_Rejects', 'Interview_Reject', 'Interview_Select'],
                                           'Candidate_quality_index_val': [Offered, HR_Rejects, Interview_Reject, Interview_Select],
                                           'Candidate_Intimacy': ['Joined', 'Rejected', 'Accepted', 'Offered'],
                                           'Candidate_Intimacy_value': [Joined, Rejected, Accepted, Offered],
                                           'table': table}
                  )


def login_dash(request):
    return render(request, 'login_dash.html')


def tables_dash(request):
    table = Staging.objects.all()
    return render(request, 'tables.html', {'table': table})


def utilities_animation(request):
    return render(request, 'utilities-animation.html')


def utilities_border(request):
    return render(request, 'utilities-border.html')


def utilities_color(request):
    return render(request, 'utilities-color.html')


def utilities_other(request):
    return render(request, 'utilities-other.html')


def error_404(request):
    return render(request, '404.html')


def blank_dash(request):
    return render(request, 'blank.html')


def buttons_dash(request):
    return render(request, 'buttons.html')


def cards_dash(request):
    return render(request, 'cards.html')


def charts_dash(request):
    cred = 'postgresql://postgres:willoffire@1@localhost:5432/Candidate'
    sqldata = pd.read_sql("""
                                SELECT *
                                FROM rlogdata_staging
                                """, con = cred)
    # for selection ration of HR
    Hr_int = sqldata[sqldata['current_status']==8]
    print(len(Hr_int.index))
    Hr_rej = sqldata[sqldata['current_status']==108]
    #print(Hr_rej)
    print(len(Hr_rej.index))
    Selection_Ratio_HR = (len(Hr_int.index)-len(Hr_rej.index))/ len(Hr_int.index)
    print("Selection_Ratio_HR: " + str(Selection_Ratio_HR))
    # end selection ration of HR

    # for selection ratio of Tech
    F2F_int = Staging.objects.filter(current_status__in = [5, 6]).count()
    F2F_int_rejects = Staging.objects.filter(current_status__in = [105, 106]).count()
    #print("this is f2f: " + str(F2F_int) + "This is f2f rejects : " + str(F2F_int_rejects))
    F2F_selection_ratio = (F2F_int - F2F_int_rejects)/F2F_int
    print("Selection Ratio Tech: ", F2F_selection_ratio)
    # end selection ration of tech

    # for final interview selection ratio
    Final_int = Staging.objects.filter(current_status = 7).count()
    Final_int_rejects = Staging.objects.filter(current_status = 107).count()
    #print("this is f2f: " + str(F2F_int) + "This is f2f rejects : " + str(F2F_int_rejects))
    Final_selection_ratio = (Final_int - Final_int_rejects)/Final_int
    print("Selection Ratio Final: ", Final_selection_ratio)

    # we use bar graph
    # end selection ratio of final interview
    
    # turn around time
    date_difference = sqldata['date_cv_submitted'] - sqldata['reqt_date']
    y = list(date_difference.dt.days.astype(int))
    counttill2 = 0
    counttill5 = 0
    counttill10 = 0
    countmore = 0
    for i in y:
            if i in range(1,3):
                counttill2 = counttill2 + 1
            if i in range(3, 6):
                counttill5 = counttill5 + 1
            if i in range(6,11):
                counttill10 = counttill10 + 1
            if i in range(11,):
                countmorethan10 = countmore + 1
                
    print(date_difference.dtypes)
        #date_difference.astype(int)
        #print(y)
    print(str(counttill2)+'  '+str(counttill5)+'   '+str(counttill10) + '   ' + str(countmorethan10))
    datecount=0
    for i in y:
            datecount = datecount + i
    #print(datecount)
    TAT = datecount/len(y)
    print('average turn around time',TAT)
    # we have to calculate the no of times i is appearing. 0 to 2, 3 to 5, 6 to 10, 10< above

        # sourcing Effectiveness
    CV_Rejected = Staging.objects.filter(current_status = 102).count()
    Duplicate_CV = Staging.objects.filter(current_status = 101).count()
    Interview_Reject = Staging.objects.filter(current_status__in = [104, 105, 106, 107, 108]).count()
    Interview_Select = Staging.objects.filter(current_status__in = [4, 5, 6, 7, 8]).count()
    CV_Shortlisted = Staging.objects.filter(current_status =  2).count()
        # sourcing effectiveness ends

        # Candidate quality index
    Offered = Staging.objects.filter(current_status = 10).count()
    HR_Rejects = Staging.objects.filter(current_status = 108).count()
        # interview reject same as above
        # interview select samw as above

        # Candidate quality index ends

        # Candidate Intimacy
    Joined = Staging.objects.filter(current_status = 14).count()
    Rejected = Staging.objects.filter(current_status__in = [102, 103, 104, 105, 106,107,108]).count()
    Accepted = Staging.objects.filter(current_status = 11).count()
        #  offered same as above

        # end of candidate intimacy



    
    return render(request, 'charts.html', {'TAT_categories': ['0-2','3-5','6-10','10 above'],
                                           'TAT_categories_value':[counttill2, counttill5, counttill10, countmorethan10],
                                           'Selection_ratio': ['HR','Tech','Final'],
                                           'Selection_ratio_value': [Selection_Ratio_HR, F2F_selection_ratio, Final_selection_ratio],
                                           'sourcing_Effectiveness':['CV_Rejected', 'Duplicate_CV', 'Interview_Reject', 'Interview_Select', 'CV_Shortlisted'],
                                           'sourcing_Effectiveness_values': [CV_Rejected, Duplicate_CV, Interview_Reject, Interview_Select, CV_Shortlisted],
                                           'Candidate_quality_index': ['Offered', 'HR_Rejects', 'Interview_Reject', 'Interview_Select'],
                                           'Candidate_quality_index_val': [Offered, HR_Rejects, Interview_Reject, Interview_Select],
                                           'Candidate_Intimacy': ['Joined', 'Rejected', 'Accepted', 'Offered'],
                                           'Candidate_Intimacy_value': [Joined, Rejected, Accepted, Offered]}
                  )
    #visualization(request)


def forgot_password(request):
    return render(request, 'forgot-password.html')


def register(request):
    return render(request, 'register.html')


def upload(request):
    return redirect('/choose')

def mandate_upload(request):
    return redirect('/mandate_choose')


def badrecords_dash(request):
    return(request,'badrecords_dash.html')


def manageteam_dash(request):
    return(request,'manageteam_dash.html')



def upload_mandate(request):
    return redirect('/mandate_choose')


def display_mandate(request):
    return(request,'display_mandate.html')

def upload_candidate(request):
    return(request,'upload_candidate.html')


def display_candidate(request):
    return(request,'display_candidate.html')


