from django.db import models
from django.contrib.auth.models import User

class py_comments(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=40,blank=False)
	email = models.CharField(max_length=40,blank=False)
	site = models.CharField(max_length=40,blank=False)
	comment = models.TextField()
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.name)

	class Admin:
		pass

