from django import forms
from .models import Ticker

class TickerForms(forms.ModelForm):
    message=forms.CharField(min_length=1,label="Введите текст бегущей строки:", widget=forms.TextInput())
    
    class Meta():
        model=Ticker
        fields=['message']