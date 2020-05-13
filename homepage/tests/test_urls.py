
from django.test import SimpleTestCase
from django.urls import reverse , resolve
from homepage.views import home , about
from django_project import urls 
from users.views import register , GroupActivitiesTable , login1 , profile , TeacherTable , DeleteTeacher , AddActivitiesGroup , AdminGroupActivitiesTable


class TestUrls(SimpleTestCase):


	def test_home_url(self):
		url = reverse('homepage-home')
		self.assertEquals(resolve(url).func , home)

	
	def test_about_url(self):
		url = reverse('homepage-about')
		self.assertEquals(resolve(url).func , about)
	

	def test_register_url(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func , register)






     
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('registerTeacher/', user_views.profile, name='registerTeacher'),
    #path('deleteTeacher/', user_views.DeleteTeacher, name='deleteTeacher'),
    #path('TeacherTable/',user_views.TeacherTable,name ='TeacherTable'),
    #path('groupActivityTable/',user_views.GroupActivitiesTable,name ='groupActivityTable'),
    #path('AdminGroupActivityTable/',user_views.AdminGroupActivitiesTable,name ='AdminGroupActivityTable'),
    #path('AddActivitiesGroup/',user_views.AddActivitiesGroup,name ='AddActivitiesGroup'),
    #path('', include('homepage.urls')),




	def test_login1_url(self):
		url = reverse('login1')
		self.assertEquals(resolve(url).func , login1)
		

	def test_registerTeacher_url(self):
		url = reverse('registerTeacher')
		self.assertEquals(resolve(url).func ,profile)


	def test_deleteTeacher_url(self):
		url = reverse('deleteTeacher')
		self.assertEquals(resolve(url).func ,DeleteTeacher)		
					

	def test_groupActivityTable_url(self):
		url = reverse('groupActivityTable')
		self.assertEquals(resolve(url).func ,GroupActivitiesTable)


	def test_AdminGroupActivityTable_url(self):
		url = reverse('AdminGroupActivityTable')
		self.assertEquals(resolve(url).func ,AdminGroupActivitiesTable)
		


	def test_AddActivitiesGroup_url(self):
		url = reverse('AddActivitiesGroup')
		self.assertEquals(resolve(url).func ,AddActivitiesGroup)				
					

	