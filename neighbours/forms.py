from django import forms
from .models import *

#various forms

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class AddHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user_profile', 'profile']


class AddBizForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['biz_owner', 'biz_hood']

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['poster', 'post_hood']

