from django.test import TestCase , Client
from django.urls import reverse 
import json


class TestViews(TestCase):

	
	def test_home(self):

		client = Client()

		responce = client.get(reverse('homepage-home'))

		self.assertEquals(responce.status_code , 200)
		self.assertTemplateUsed(responce , 'homepage/home.html')


	def test_about(self):

		client = Client()

		responce = client.get(reverse('homepage-about'))

		self.assertEquals(responce.status_code , 200)
		self.assertTemplateUsed(responce , 'homepage/about.html')