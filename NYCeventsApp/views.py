from django.shortcuts import render
from NYCeventsApp.models import *

# Create your views here.

def home(request):
    return render(request, 'NYCeventsApp/main_site.html')