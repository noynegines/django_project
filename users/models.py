from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	phone = models.CharField(max_length=10)
	t_id = models.CharField(max_length=9, unique = True)
	aboutMe=models.TextField(default='')
	
	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('login1')

class RegisterChild(models.Model):
	ID_P = models.CharField(max_length=200)
	ID_C = models.CharField(max_length=9)
	FName_C = models.CharField(max_length=20)
	LName_C = models.CharField(max_length=20)
	Age_C  = models.CharField(max_length=10)
	Phone_P = models.CharField(max_length=10)
	idClass = models.CharField(max_length=10)

class HoursReport(models.Model):
	t_id = models.CharField(max_length=9)
	start_hour=models.CharField(max_length=20)
	finish_hour=models.CharField(max_length=20)
	date=models.CharField(max_length=20)
