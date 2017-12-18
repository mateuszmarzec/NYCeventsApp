from django.shortcuts import render
from NYCeventsApp.models import *
from loadDataFromGoogle import query_shakespeare

# Create your views here.

def home(request):

    response = query_shakespeare("""SELECT TIMESTAMP_TRUNC(pickup_datetime,
                      MONTH) month,
                      COUNT(*) trips
                      FROM `bigquery-public-data.new_york.tlc_yellow_trips_2015`
                      GROUP BY 1
                      ORDER BY 1""")


    return render(request, 'NYCeventsApp/main_site.html', {'response':response})


