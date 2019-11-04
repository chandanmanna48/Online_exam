from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
#from django.contrib.auth.models import User
from .models import Student
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('gender','phoneno','dob','profile_image','college_name','branch')


class ProfileForm(forms.Form):
    image = forms.ImageField()
