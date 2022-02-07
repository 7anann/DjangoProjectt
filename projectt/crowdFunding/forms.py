from django import forms
from .models import myuser

class RegisterationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=myuser
        exclude = ('country','birthdate', 'fb_account')



class loginForm(forms.ModelForm):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=myuser
        fields= ['Email','password']

class EditForm(forms.ModelForm):
    class Meta:
        model = myuser
        exclude = ('Email','profile_picture','confirm_password')