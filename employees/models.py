from django.db import models

# Create your models here.
class Employee(models.Model):
	Gender_choices=[
	('M','Male'),
	('F', 'Female'),
	]

	First_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=50, blank=True)
	Email_id = models.EmailField()
	Phone = models.CharField(max_length=20)
	Gender = models.CharField(choices=Gender_choices, max_length=30)
	Address = models.TextField(max_length=100)
	job = models.ManyToManyField('AvailableJobs',blank=True)
	DOB = models.DateField()


class AvailableJobs(models.Model):
	name = models.CharField(max_length=100)


	def __str__(self):
		return self.name
