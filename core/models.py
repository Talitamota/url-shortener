from django.db import models

from core.utils import gera_hash

class Url(models.Model):
	url_original = models.URLField()
	url_hash = models.CharField(max_length=10)

	def save(self):
		if not self.id:
			self.url_hash = gera_hash()
		super(Url, self).save()

	def gera_url_encurtada(self):
		return 'http://localhost:8000/'+self.url_hash

	def __str__(self):
		return self.url_original

