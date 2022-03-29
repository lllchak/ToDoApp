from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .utils import *


class TasksHome(DataMixin, ListView):
	model = Tasks
	template_name = 'ToDoApp/tasks.html'
	context_object_name = 'tasks'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Все таски')
		return dict(list(context.items()) + list(c_def.items()))

	def get_queryset(self):
		return Tasks.objects.all()


def index(request):
	context = {
		'title': 'Главная страница',
	}
	return render(request, 'ToDoApp/index.html', context)


def show_category(request, cat_id):
	context = {
		'title': f"Категория {cat_id}",
		'tasks': Tasks.objects.filter(cat_id=cat_id),
		'cat_selected': cat_id,
	}
	return render(request, 'ToDoApp/tasks.html', context)


def profile(request):
	context = {
		'title': 'Страница профиля',
	}
	return render(request, 'ToDoApp/profile.html', context)


class Create(LoginRequiredMixin, DataMixin, CreateView):
	form_class = AddTaskForm
	template_name = 'ToDoApp/create.html'
	success_url = reverse_lazy('tasks')
	login_url = reverse_lazy('home')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Создание таска')
		return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
	form_class = RegisterUserForm
	template_name = 'ToDoApp/register.html'
	success_url = reverse_lazy('login')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Регистрация')
		return dict(list(context.items()) + list(c_def.items()))

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('home')


class LoginUser(DataMixin, LoginView):
	form_class = LoginUserForm
	template_name = 'ToDoApp/login.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Вход')
		return dict(list(context.items()) + list(c_def.items()))

	def get_success_url(self):
		return reverse_lazy('home')


def logout_user(request):
	logout(request)
	return redirect('login')


def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>Странца не найдена</h1>')
