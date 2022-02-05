from django import forms
from .models import myuser

class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=myuser
        fields= '__all__'



class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=myuser
        fields= ['Email','password']

class EditForm(forms.ModelForm):
    class Meta:
        model = myuser
        exclude = ('Email',)