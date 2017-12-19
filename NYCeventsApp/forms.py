from django import forms


class SelectEventForm(forms.Form):
   start_date = forms.CharField()
   end_date = forms.CharField()