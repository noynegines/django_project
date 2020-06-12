from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	phone = models.CharField(max_length=10)
	t_id = models.CharField(max_length=9, unique = True)
	aboutMe=models.TextField(default='')


	

	
	
	
	
	
	def __str__(self):
		return self.user.username+self.phone+self.t_id+self.aboutMe

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
	def __str__(self):
			return self.ID_P + self.ID_C +self.FName_C+self.LName_C+self.Age_C+self.Phone_P+self.idClass

class HoursReport(models.Model):
	t_id = models.CharField(max_length=9)
	start_hour=models.CharField(max_length=20)
	finish_hour=models.CharField(max_length=20)
	date=models.CharField(max_length=20)

	def __str__(self):
			return self.t_id + self.start_hour + self.finish_hour + self.date
