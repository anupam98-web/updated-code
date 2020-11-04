from django.shortcuts import render, redirect
from .models import Mandate
from rlogsystem.models import CandidateStatus
from .resources import JobResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse, JsonResponse
from .forms import MandateForm
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json
import os
import datetime
from pprint import pprint
#  from django.contrib.staticfiles.templatetags.staticfiles import static # no such file
from django.forms.models import model_to_dict
# from django.contrib.auth.views import login,logout # cannot import name 'login' from 'django.contrib.auth.views'

# Create your views here.
CSV_STORAGE = os.path.join(os.getcwd(), 'database', 'static', 'csv')


@csrf_exempt
def import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students) #make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/fieldmatching?df='+ path_name)
    else:
        return render(request, 'import_data.html')


def fieldmatching(request):   
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Mandate._meta.get_fields()]
        if request.POST.get('checkBox') == None:   
        #  To keep the same columns in case of matching 'fields' and ###'names', add a checkbox on the html page
            matched = { key:request.POST.get(key, False) for key in fields }
            new_dict = dict([(value, key) for key, value in matched.items()])
            df.rename(columns = new_dict, inplace = True)
        #  df.drop('id', axis=1, inplace=True) # Drop Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names. When using a multi-index, labels on different levels can be removed by specifying the level.
        #  Set the DataFrame index (row labels) using one or more existing columns or arrays (of the correct length). The index can replace the existing index or expand on it.
        #  "None of ['apple', 'ball', 'cat', 'dog', 'eagle', 'fox', 'gorrila', 'hen', 'int', 'jet', 'kite', 'lamba', 'mamba', 'next', 'o', 'p'] are in the columns"
        #  Convert the DataFrame to a dictionary. orientation 
        #  df.to_dict('index') return this > {'row1': {'col1': 1, 'col2': 0.5}, 'row2': {'col1': 2, 'col2': 0.75}} 
    
        df.set_index('id', drop=True, inplace=True)
        dictionary = df.to_dict(orient="index")
        print(dictionary)
    
###
        for index, object in dictionary.items():
            # model = MODEL_NAME()
            model = Mandate()
            for key,value in object.items():
                setattr(model, key, value)
            setattr(model, 'id', index)
            model.save()
###            
        return render(request, 'import_data.html')
# i m getting an error when in use return redirect('import_data')
    else:
        path_name = request.GET.get('df')
        df = pd.read_csv(path_name)
        names = list(df.columns)
        print(names)
        fields = [field.name for field in Mandate._meta.get_fields()]
        #df['date'].dtype
        #df['date']= pd.to_datetime(df['date'])
        #df['month_of_date'] = df['date'].dt.month
        #df['day'] = df['date'].dt.day
        #print(df['day'])
        #print(df['month_of_date'])
        #print(list(df.columns)
        #CandidateStatus.objects.values_list('StageName', flat = True)
        df[['Current Status Nos','Status Description']] = df[['Current Status Nos','Status Description']].fillna('')
        print(df)
        for index, row in df.iterrows():

            if row['Current Status Nos'] == '' and row['Status Description'] == CandidateStatus.objects.only('StageName').get(pk=1).StageName:
                df.at[0,'Current Status Nos']= CandidateStatus.objects.only('StageID').get(pk=1).StageID
                pass
            elif row['Current Status Nos'] == CandidateStatus.objects.only('StageID').get(pk=1).StageID and row['Status Description']== '':
                df.at[0,'Status Description']= CandidateStatus.objects.only('StageName').get(pk=1).StageName
                pass
            if row['Current Status Nos'] == '' and row['Status Description'] == CandidateStatus.objects.only('StageName').get(pk=2).StageName:
                df.at[1,'Current Status Nos']= CandidateStatus.objects.only('StageID').get(pk=2).StageID 
            elif row['Current Status Nos'] == CandidateStatus.objects.only('StageID').get(pk=2).StageID and row['Status Description']== '':
                df.at[1,'Status Description']= CandidateStatus.objects.only('StageName').get(pk=2).StageName
            if row['Current Status Nos'] == '' and row['Status Description'] == CandidateStatus.objects.only('StageName').get(pk=3).StageName:
                df.at[2,'Current Status Nos']= CandidateStatus.objects.only('StageID').get(pk=3).StageID 
            elif row['Current Status Nos'] == CandidateStatus.objects.only('StageID').get(pk=3).StageID and row['Status Description']== '':
                df.at[2,'Status Description']= CandidateStatus.objects.only('StageName').get(pk=3).StageName
            if row['Current Status Nos'] == '' and row['Status Description'] == CandidateStatus.objects.only('StageName').get(pk=4).StageName:
                df.at[3,'Current Status Nos']= CandidateStatus.objects.only('StageID').get(pk=4).StageID 
            elif row['Current Status Nos'] == CandidateStatus.objects.only('StageID').get(pk=4).StageID and row['Status Description']== '':
                df.at[3,'Status Description']= CandidateStatus.objects.only('StageName').get(pk=4).StageName
            if row['Current Status Nos'] == '' and row['Status Description'] == CandidateStatus.objects.only('StageName').get(pk=5).StageName:
                df.at[4,'Current Status Nos']= CandidateStatus.objects.only('StageID').get(pk=5).StageID 
            elif row['Current Status Nos'] == CandidateStatus.objects.only('StageID').get(pk=5).StageID and row['Status Description']== '':
                df.at[4,'Status Description']= CandidateStatus.objects.only('StageName').get(pk=5).StageName
            elif row['Current Status Nos'] == '' and row['Status Description']== 'F2F Interview 1':
                df.at[5,'Current Status Nos']= 5
            elif row['Current Status Nos'] == int(5) and row['Status Description']== '':
                df.at[5,'Status Description']= 'F2F Interview 1'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'F2F Interview 2':
                df.at[6,'Current Status Nos']= 6
            elif row['Current Status Nos'] == int(6) and row['Status Description']== '':
                df.at[6,'Status Description']= 'F2F Interview 2'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Final Interview':
                df.at[7,'Current Status Nos']= 7
            elif row['Current Status Nos'] == int(7) and row['Status Description']== '':
                df.at[7,'Status Description']= 'Final Interview'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'HR Interview':
                df.at[8,'Current Status Nos']= 8
            elif row['Current Status Nos'] == int(8) and row['Status Description']== '':
                df.at[8,'Status Description']= 'HR Interview'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Offer Awaited':
                df.at[9,'Current Status Nos']= 9
            elif row['Current Status Nos'] == int(9) and row['Status Description']== '':
                df.at[9,'Status Description']= 'Offer Awaited'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Offered':
                df.at[10,'Current Status Nos']= 10
            elif row['Current Status Nos'] == int(10) and row['Status Description']== '':
                df.at[10,'Status Description']= 'Offered'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Offer Accepted':
                df.at[11,'Current Status Nos']= 11
            elif row['Current Status Nos'] == int(11) and row['Status Description']== '':
                df.at[11,'Status Description']= 'Offer Accepted'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Follow for Joining':
                df.at[12,'Current Status Nos']= 12
            elif row['Current Status Nos'] == int(12) and row['Status Description']== '':
                df.at[12,'Status Description']= 'Follow for Joining'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Offer on Hold':
                df.at[13,'Current Status Nos']= 13
            elif row['Current Status Nos'] == int(13) and row['Status Description']== '':
                df.at[13,'Status Description']= 'Offer on Hold'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Joined ':
                df.at[14,'Current Status Nos']= 14
            elif row['Current Status Nos'] == int(14) and row['Status Description']== '':
                df.at[14,'Status Description']= 'Joined '
            elif row['Current Status Nos'] == '' and row['Status Description']== 'On Hold':
                df.at[15,'Current Status Nos']= 15
            elif row['Current Status Nos'] == int(15) and row['Status Description']== '':
                df.at[15,'Status Description']= 'On Hold'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Reqt On Hold':
                df.at[16,'Current Status Nos']= 16
            elif row['Current Status Nos'] == int(16) and row['Status Description']== '':
                df.at[16,'Status Description']= 'Reqt On Hold'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Reqt Dead':
                df.at[17,'Current Status Nos']= 17
            elif row['Current Status Nos'] == int(17) and row['Status Description']== '':
                df.at[17,'Status Description']= 'Reqt Dead'
            elif row['Current Status Nos'] == '' and row['Status Description']== 'Candidate Withdrawn':
                df.at[18,'Current Status Nos']= 18
            elif row['Current Status Nos'] == int(18) and row['Status Description']== '':
                df.at[18,'Status Description']= 'Candidate Withdrawn'    
                    
        print(df)

        return render(request, 'fieldmatching.html', {'fields' : names, 'path_name': path_name, 'names' : fields})












         
        
        
        
        
        
        
         
       
