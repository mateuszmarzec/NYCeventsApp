from django import forms
from NYCeventsApp.models import *

CHOICES_EVENT = []

CHOICES_EVENT = [[0 for x in range(2)] for y in range(len(Events.objects.all()))]
i = 0
for event in Events.objects.all():
    CHOICES_EVENT[i][0] = event.id
    CHOICES_EVENT[i][1] = event.name + ' vs ' + event.additional + ' ' + str(event.date)
    i = i+1

CHOICES_OUTPUT = (
    ('GOOGLE_MAP', 'GOOGLE MAP'),
    ('HOUR_BY_HOUR_PLOT', 'HOUR BY HOUR PLOT'),
)


class SelectEventForm(forms.Form):
    switch_direction = forms.BooleanField(required=False ,label='', widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    choose_event = forms.ChoiceField(label='',choices=CHOICES_EVENT, widget=forms.Select(attrs={'class':'form-control'}))
    choose_output = forms.ChoiceField(label='',choices=CHOICES_OUTPUT, widget=forms.Select(attrs={'class':'form-control'}))
