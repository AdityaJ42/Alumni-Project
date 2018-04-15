from django import forms
from .models import Events


class eventForm(forms.ModelForm):
    date = forms.DateField(widget = forms.SelectDateWidget)

    class Meta:
        model = Events
        fields = ['event_name', 'location', 'description', 'date']
