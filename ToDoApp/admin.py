from django.contrib import admin
from .models import *


class TasksAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'time_create')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'content')
	list_filter = ('time_create',)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')
	search_fields = ('name',)
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tasks, TasksAdmin)
admin.site.register(Category, CategoryAdmin)
