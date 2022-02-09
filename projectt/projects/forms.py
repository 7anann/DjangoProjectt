from django.forms import ModelForm
from django import forms
from .models import *
from django.core.validators import RegexValidator


class SearchForm(forms.Form):
    mode = forms.ChoiceField(required=True,choices=(('1',"Tage"),('2',"title")))
    search = forms.CharField(required=True)
class ReportForm(forms.Form):
    content = forms.CharField(required=True)
#=======================================
