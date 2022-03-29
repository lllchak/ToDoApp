from django.db import models

# каждый экземпляр этого класса это одна запись (строка) в исходной таблице
from django.urls import reverse


class Tasks(models.Model):

	class Meta:
		verbose_name = 'Все таски'
		verbose_name_plural = 'Все таски'
		ordering = ['-time_create', 'title']

	title = models.CharField(max_length=255, verbose_name='Название таска')
	content = models.TextField(blank=True, verbose_name='Описание')
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
	cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

	def __str__(self):
		return self.title


class Category(models.Model):

	class Meta:
		verbose_name = 'Категории'
		verbose_name_plural = 'Категории'
		ordering = ['id']

	name = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_id': self.pk})
