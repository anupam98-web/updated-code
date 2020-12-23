from django.shortcuts import render, redirect
from dashboard import views
from mapping import views
from rlogdata.models import Staging
from mapping.views import visualization
from rlogdata.models import *
import pandas as pd


# Create your views here.

def home(request):
    return render(request, 'index_dash.html')


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
    return render(request, 'charts.html', {'TAT_categories': ['0-2','3-5','6-10','10 above'],
                                           'TAT_categories_value':[counttill2, counttill5, counttill10, countmorethan10]}
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


