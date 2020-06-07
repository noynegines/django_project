from django.test import TestCase , Client
from django.urls import reverse 
import json
from django.contrib.auth.models import User
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import SimpleTestCase, Client, RequestFactory, TestCase
from django.urls import reverse , resolve
from homepage.views import home , about
from django_project import urls
from users.models import RegisterChild
from users.views import register , GroupActivitiesTable , login1 , profile , TeacherTable , DeleteTeacher , AddActivitiesGroup , AdminGroupActivitiesTable ,registerToClass,showMyClasses,editDetails,ShowMyClass,Admin_Edit_Class,Admin_Delete_Class,GuideShowRegistersByClass,adminShowRegisters,adminShowRegistersByMatnas



class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.registerToClass2 = ('registerToClass')
		self.user_login = {'username': 'test', 'password':'!!!123TEST'}
		self.user_admin = {'username': 'test1', 'password':'!!!123TEST1'}
		self.user = User.objects.create_user(**self.user_login)
		self.user.save()
		self.user_admin = User.objects.create_superuser(**self.user_admin)
		self.user.save()
		self.registerToClass1 = RegisterChild(ID_P = '123456789', ID_C = '987654321', FName_C = 'test2', LName_C = 'TEST2', Age_C = '6', Phone_P = '0544351443', idClass = '1')
		self.registerToClass1.save()
		self.factory = RequestFactory()

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

	def test_registerToClass1(self):
	 	request = self.factory.get('simpleuser/registerToClass.html')
	 	self.client.force_login(self.user)
	 	request.user = self.user
	 	middleware = SessionMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()
	 	middleware = MessageMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()

	 	response = self.client.get(registerToClass(request), follow = True)
	 	self.assertEqual(response.status_code, 404)


	def test_GroupActivitiesTable1(self):
	 	request = self.factory.get('simpleuser/GroupActivitiesTable.html')
	 	self.client.force_login(self.user)
	 	request.user = self.user
	 	middleware = SessionMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()
	 	middleware = MessageMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()

	 	response = self.client.get(GroupActivitiesTable(request), follow = True)
	 	self.assertEqual(response.status_code, 404)

	def test_showMyClasses1(self):
	 	request = self.factory.get('simpleuser/showMyClasses.html')
	 	self.client.force_login(self.user)
	 	request.user = self.user
	 	middleware = SessionMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()
	 	middleware = MessageMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()

	 	response = self.client.get(showMyClasses(request), follow = True)
	 	self.assertEqual(response.status_code, 404)

	def test_AdminGroupActivitiesTable1(self):
	 	request = self.factory.get('Admin1/showGroupActivies.html')
	 	self.client.force_login(self.user_admin)
	 	request.user_admin = self.user_admin
	 	middleware = SessionMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()
	 	middleware = MessageMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()

	 	response = self.client.get(AdminGroupActivitiesTable(request), follow = True)
	 	self.assertEqual(response.status_code, 404)

	def test_adminShowRegisters1(self):
	 	request = self.factory.get('Admin1/showRegisters.html')
	 	self.client.force_login(self.user_admin)
	 	request.user_admin = self.user_admin
	 	middleware = SessionMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()
	 	middleware = MessageMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()

	 	response = self.client.get(adminShowRegisters(request), follow = True)
	 	self.assertEqual(response.status_code, 404)

	def test_adminShowRegistersByMatnas1(self):
	 	request = self.factory.get('Admin1/showRegistersByMatnas.html')
	 	self.client.force_login(self.user_admin)
	 	request.user_admin = self.user_admin
	 	middleware = SessionMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()
	 	middleware = MessageMiddleware()
	 	middleware.process_request(request)
	 	request.session.save()

	 	response = self.client.get(adminShowRegistersByMatnas(request), follow = True)
	 	self.assertEqual(response.status_code, 404)