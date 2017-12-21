from django import forms
from NYCeventsApp.models import *

CHOICES = []

CHOICES = [[0 for x in range(2)] for y in range(len(Events.objects.all()))]
i = 0
for event in Events.objects.all():
    CHOICES[i][0] = event.id
    CHOICES[i][1] = event.name + ' vs ' + event.additional + ' ' + str(event.date)
    i = i+1

class SelectEventForm(forms.Form):
    switch_direction = forms.BooleanField(required=False ,label='', widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    choose_event = forms.ChoiceField(label='',choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
