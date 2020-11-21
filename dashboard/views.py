from django.shortcuts import render, redirect
from dashboard import views
from mapping import views
from rlogdata.models import Staging


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
    return render(request, 'charts.html')


def forgot_password(request):
    return render(request, 'forgot-password.html')


def register(request):
    return render(request, 'register.html')


def upload(request):
    return redirect('/choose')

def mandate_upload(request): # your edit
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


