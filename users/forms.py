from django import forms
from users.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from users.models import User


 
# class UserChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['map_style','distance_units','phone','facebook','whatsapp','linkedin']


# class UserForm(forms.ModelForm): 
#     class Meta:
#         model = User
#         fields = ['email' ,'first_name','last_name','username']


# class ProfilePictureForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['profile_pic']


# class FollowupForm(forms.ModelForm):
#     class Meta:
#         model = Followup_Form
#         fields = ['date','note']


# class UserLocationForm(forms.ModelForm): 
#     class Meta:
#         model = User
#         fields = ['address' ,'city','state','country','latitude','longtitude']