from django.urls import path, re_path

from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('profile/', profile, name='profile'),
	path('create/', Create.as_view(), name='create'),
	path('login/', LoginUser.as_view(), name='login'),
	path('logout/', logout_user, name='logout'),
	path('register/', RegisterUser.as_view(), name='register'),
	path('tasks/', TasksHome.as_view(), name='tasks'),
	path('category/<int:cat_id>/', show_category, name='category'),
]