from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Tweet, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control w-100',
                                                           'id': 'contentsBox', 'rows': '3',
                                                           'placeholder': "What's happening?"}))

    class Meta:
        model = Tweet
        fields = ['content']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
