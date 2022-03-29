from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddTaskForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['cat'].empty_label = 'Выбрать'

	class Meta:
		model = Tasks
		fields = ['title', 'content', 'cat']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control', 'cols': 20, 'rows': 3}),
			'cat': forms.Select(attrs={'class': 'form-select'})
		}


class AddCatForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = Category
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'})
		}


class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-input'}),
			'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
			'password2': forms.PasswordInput(attrs={'class': 'form-input'})
		}


class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		fields = ('username', 'password')
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-input'}),
			'password': forms.PasswordInput(attrs={'class': 'form-input'})
		}
