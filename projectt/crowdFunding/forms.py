from django import forms
from .models import myuser

class RegisterationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=myuser
        exclude = ('country','birthdate', 'fb_account')



class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=myuser
        fields= ['Email','password']

class EditForm(forms.ModelForm):
    class Meta:
        model = myuser
        #fields= ['first_name','last_name','country','password', 'birthdate','phone_number']
        #fields = ['first_name','last_name','country','password','phone_number','birthdate','fb_account']
        #fields='__all__'
        exclude = ('Email','profile_picture','confirm_password')