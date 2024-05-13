from django import forms
from django.forms import DateTimeField, ModelForm
from django.contrib.auth.forms import UserCreationForm
 

from .models import *
# from farmer.models import * 


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'email', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2', 
            ]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar',
            'email', 
            'first_name', 
            'last_name',
            'nrc',
            'phone', 
            'location', 
            'country'
            ]


class ApointmentForm(forms.ModelForm):
    startTime = forms.SplitDateTimeField()
    endtTime = forms.SplitDateTimeField()
    class Meta:
        model = Apointment
        fields = [
            'subject',
            'startTime', 
            'endtTime', 
            ]



#lawyerForm

