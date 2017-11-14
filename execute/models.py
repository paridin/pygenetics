from django.db import models
from django.contrib.auth.models import User

class py_results(models.Model):
    user= models.ForeignKey(User)
    time = models.DecimalField(max_digits=15,decimal_places=13)
    best_time = models.DecimalField(max_digits=15,decimal_places=13)
    generation_id = models.IntegerField()
    best_fitness = models.IntegerField()
    type_tuning = models.CharField(max_length=40,blank=False)
    mut_percent = models.IntegerField()
    cross_percent = models.IntegerField()
    num_gen = models.IntegerField()
    name_file = models.CharField(max_length=40,blank=False)

    def __str__(self):
        return str(self.user) + ":" + str(self.type_tuning)

    def get_user(self,id__):
        return User.objects.get(id=id__)

	def last_file(self):
		return str(py_results.objects.latest('name_file'))

    class Admin:
        pass

class py_averages(models.Model):
	name_file = models.CharField(max_length=40,blank=False)
	time_average = models.DecimalField(max_digits=15,decimal_places=13)
	fitness_average = models.DecimalField(max_digits=15,decimal_places=10)

	def __str__(self):
		return str(self.name_file)+":"+str(self.time_average)+":"+str(self.fitness_average)

	class Admin:
		pass

