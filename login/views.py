from django.shortcuts import render,redirect
from login import views
from django.http import HttpResponse
from rlogdata.models import *
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.template import Context


# Create your views here.
def login_page(request):
	return render(request,'index_login.html')

def user_login(request):
	if request.method=="POST":
		username =request.POST.get('username')
		password=request.POST.get('password')
		x=authenticate(request, username=username, password=password)
		print(x)
		if x is None:

			return redirect('/login/')

		else:
			login(request,x)
			return render(request,'index_dash.html')
