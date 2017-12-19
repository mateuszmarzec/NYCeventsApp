from django.shortcuts import render
from NYCeventsApp.models import *
from loadDataFromGoogle import query_shakespeare
from NYCeventsApp import forms



# Create your views here.

def home(request):
    if request.method =='POST':
        form = forms.SelectEventForm(request.POST)
        if form.is_valid():

            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']

            sql_request = """SELECT pickup_latitude, pickup_longitude FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015` WHERE pickup_datetime > TIMESTAMP (@start_date) 
            AND pickup_datetime < TIMESTAMP(@end_date) AND pickup_longitude <> 0 AND dropoff_latitude <= 40.7128 AND dropoff_latitude >= 40.7127"""

            response = query_shakespeare(sql_request, start, end)

            return render(request, 'NYCeventsApp/main_site.html', {'response':response, 'form':form})

    form = forms.SelectEventForm()
    return render(request, 'NYCeventsApp/main_site.html', {'form':form})

