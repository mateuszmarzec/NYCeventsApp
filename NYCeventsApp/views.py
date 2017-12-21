from django.shortcuts import render
from NYCeventsApp.models import *
from loadDataFromGoogle import query_shakespeare
from NYCeventsApp import forms
from django.shortcuts import get_object_or_404
import datetime

def home(request):
    if request.method =='POST':
        form = forms.SelectEventForm(request.POST)
        if form.is_valid():

            event_id = form.cleaned_data['choose_event']
            event = get_object_or_404(Events, id=event_id)
            switch_direction = form.cleaned_data['switch_direction']

            coordinates = {'latitude': event.latitude, 'longitude': float(event.longitude)}

            if switch_direction:
                start = str(event.date - datetime.timedelta(hours=2))
                end = str(event.date)

                sql_request = """SELECT dropoff_latitude, dropoff_longitude FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015`
                                 WHERE dropoff_datetime > TIMESTAMP (@start_date) AND dropoff_datetime < TIMESTAMP(@end_date)
                                 AND dropoff_longitude <> 0 AND pickup_latitude <= @lat + 0.001 AND pickup_latitude >= @lat - 0.001
                                 AND pickup_longitude <= @lng + 0.001 AND pickup_longitude >= @lng - 0.001
                                 """
            else:

                event_duration = datetime.datetime.combine(datetime.date.min, event.time) - datetime.datetime.min

                start = str(event.date + event_duration)
                end = str(event.date + event_duration + datetime.timedelta(hours=2))

                sql_request = """SELECT pickup_latitude, pickup_longitude FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015`
                                 WHERE pickup_datetime > TIMESTAMP (@start_date) AND pickup_datetime < TIMESTAMP(@end_date)
                                 AND pickup_longitude <> 0 AND dropoff_latitude <= @lat + 0.001 AND dropoff_latitude >= @lat - 0.001
                                 AND dropoff_longitude <= @lng + 0.001 AND dropoff_longitude >= @lng - 0.001
                                 """

            response = query_shakespeare(sql_request, start, end, coordinates)

            return render(request, 'NYCeventsApp/main_site.html', {'response':response, 'form':form,
                                                                 'longitude':coordinates['longitude'],
                                                                  'latitude': coordinates['latitude']})

    form = forms.SelectEventForm()
    return render(request, 'NYCeventsApp/main_site.html', {'form':form})

