from django.db import models

class Quote(models.Model):

	name = models.CharField('Название новостя', max_length=100, blank=True, null=True)
	descriptions = models.TextField('Описание', null=True)
	Time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

