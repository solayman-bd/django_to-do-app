from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import TaskModel


class RegisterForm(UserCreationForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email= forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model=User
        # fields="__all__"
        fields=['username','first_name','last_name','email']
        



class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']