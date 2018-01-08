from django.shortcuts import render
from NYCeventsApp.models import *
from loadDataFromGoogle import query_shakespeare
from NYCeventsApp import forms
from django.shortcuts import get_object_or_404
import datetime
import requests
from collections import Counter
import operator

def home(request):
    if request.method =='POST':
        form = forms.SelectEventForm(request.POST)
        if form.is_valid():
            counts = 0
            event_id = form.cleaned_data['choose_event']
            event = get_object_or_404(Events, id=event_id)
            switch_direction = form.cleaned_data['switch_direction']
            type = form.cleaned_data['choose_output']

            coordinates = {'latitude': event.latitude, 'longitude': float(event.longitude)}
            source = "bigquery-public-data.new_york.tlc_yellow_trips_" + str(event.date.year)
            print(source)
            if switch_direction:

                event_duration = datetime.datetime.combine(datetime.date.min, event.time) - datetime.datetime.min

                start = str(event.date + event_duration)
                end = str(event.date + event_duration + datetime.timedelta(hours=2))

                if type == ('GOOGLE_MAP' or 'BY_STREET1' or 'BY_STREET2'):

                    sql_request = """SELECT dropoff_latitude, dropoff_longitude FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015`
                                     WHERE dropoff_datetime > TIMESTAMP (@start_date) AND dropoff_datetime < TIMESTAMP(@end_date)
                                     AND dropoff_longitude <> 0 AND pickup_latitude <= @lat + 0.001 AND pickup_latitude >= @lat - 0.001
                                     AND pickup_longitude <= @lng + 0.001 AND pickup_longitude >= @lng - 0.001
                                     """
                if type == 'HOUR_BY_HOUR_PLOT':
                    # for charts
                    sql_request = """SELECT  TIMESTAMP_TRUNC(dropoff_datetime, minute), COUNT(*) FROM( 
                                     SELECT dropoff_latitude, dropoff_longitude, dropoff_datetime FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015`
                                     WHERE dropoff_datetime > TIMESTAMP (@start_date) AND dropoff_datetime < TIMESTAMP(@end_date)
                                     AND dropoff_longitude <> 0 AND pickup_latitude <= @lat + 0.001 AND pickup_latitude >= @lat - 0.001
                                     AND pickup_longitude <= @lng + 0.001 AND pickup_longitude >= @lng - 0.001 )
                                     GROUP BY 1 ORDER BY 1
                                     """
            else:
                start = str(event.date - datetime.timedelta(hours=2))
                end = str(event.date)

                if type == ('GOOGLE_MAP' or 'BY_STREET1' or 'BY_STREET2'):
                    sql_request = """SELECT pickup_latitude, pickup_longitude FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015`
                                     WHERE pickup_datetime > TIMESTAMP (@start_date) AND pickup_datetime < TIMESTAMP(@end_date)
                                     AND pickup_longitude <> 0 AND dropoff_latitude <= @lat + 0.001 AND dropoff_latitude >= @lat - 0.001
                                     AND dropoff_longitude <= @lng + 0.001 AND dropoff_longitude >= @lng - 0.001
                                     """
                if type == 'HOUR_BY_HOUR_PLOT':
                    # for charts
                    sql_request = """SELECT TIMESTAMP_TRUNC(pickup_datetime, minute), COUNT(*) FROM (
                                     SELECT pickup_latitude, pickup_longitude, pickup_datetime FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015`
                                     WHERE pickup_datetime > TIMESTAMP (@start_date) AND pickup_datetime < TIMESTAMP(@end_date)
                                     AND pickup_longitude <> 0 AND dropoff_latitude <= @lat + 0.001 AND dropoff_latitude >= @lat - 0.001
                                     AND dropoff_longitude <= @lng + 0.001 AND dropoff_longitude >= @lng - 0.001)
                                     GROUP BY 1 ORDER BY 1
                                     """

            response = query_shakespeare(sql_request, start, end, coordinates, source)

            if type == ('BY_STREET1' or 'BY_STREET2'):
                addr_arr = []
                for row in response:
                    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={row1},{row2}&sensor=false&key=AIzaSyDqZXQrRSkucJiWKx7eadH7qfv29uUFXno'.format(row1=row[0], row2=row[1]))
                    if api_response.status_code == 200:
                        addr_arr.append(api_response.json()['results'][0]['address_components'][1]['short_name'])
                counts = dict(sorted(dict(Counter(addr_arr)).items(), key=operator.itemgetter(1), reverse=True))


            return render(request, 'NYCeventsApp/main_site.html', {'response':response, 'type':type, 'form':form,
                                                                 'longitude':coordinates['longitude'],
                                                                  'latitude': coordinates['latitude'], 'counts':counts})

    form = forms.SelectEventForm()
    return render(request, 'NYCeventsApp/main_site.html', {'form':form})

