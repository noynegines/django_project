
from django.test import  TestCase
from django.urls import reverse , resolve
from homepage.views import home , about
from users.views import register , GroupActivitiesTable , login1 , profile , TeacherTable , DeleteTeacher , AddActivitiesGroup , AdminGroupActivitiesTable ,registerToClass,showMyClasses,editDetails,ShowMyClass,Admin_Edit_Class,Admin_Delete_Class,GuideShowRegistersByClass,adminShowRegisters,adminShowRegistersByMatnas , simpleuserDetailGuideS , adminDeleteChildFromClass  , tableReportGuide , HoursReportGuid


class TestUrls(TestCase):



	def test_home_url(self):
		url = reverse('homepage-home')
		self.assertEquals(resolve(url).func , home)


	def test_about_url(self):
	 	url = reverse('homepage-about')
	 	self.assertEquals(resolve(url).func , about)


	def test_register_url(self):
	 	url = reverse('register')
	 	self.assertEquals(resolve(url).func , register)


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


	def test_TeacherTable(self):
	 	url = reverse('TeacherTable')
	 	self.assertEquals(resolve(url).func ,TeacherTable)

	def test_registerToClass(self):
	 	url = reverse('registerToClass')
	 	self.assertEquals(resolve(url).func ,registerToClass)

	def test_showMyClasses(self):
	 	url = reverse('showMyClasses')
	 	self.assertEquals(resolve(url).func ,showMyClasses)

	def test_editDetails(self):
	 	url = reverse('editDetails')
	 	self.assertEquals(resolve(url).func ,editDetails)

	def test_ShowMyClass(self):
	 	url = reverse('ShowMyClass')
	 	self.assertEquals(resolve(url).func ,ShowMyClass)

	def test_Admin_Edit_Class(self):
	 	url = reverse('Admin_Edit_Class')
	 	self.assertEquals(resolve(url).func ,Admin_Edit_Class)

	def test_Admin_Delete_Class(self):
	 	url = reverse('Admin_Delete_Class')
	 	self.assertEquals(resolve(url).func ,Admin_Delete_Class)

	def test_GuideShowRegistersByClass(self):
	 	url = reverse('GuideShowRegistersByClass')
	 	self.assertEquals(resolve(url).func ,GuideShowRegistersByClass)

	def test_AdminShowRegisters(self):
	 	url = reverse('AdminShowRegisters')
	 	self.assertEquals(resolve(url).func ,adminShowRegisters)

	def test_showRegistersByMatnas(self):
	 	url = reverse('showRegistersByMatnas')
	 	self.assertEquals(resolve(url).func, adminShowRegistersByMatnas)


	def test_simpleuserDetailGuideS(self):
	 	url = reverse('DetailGuideS')
	 	self.assertEquals(resolve(url).func, simpleuserDetailGuideS)


	def test_adminDeleteChildFromClass(self):
	 	url = reverse('DeleteChildFromClass')
	 	self.assertEquals(resolve(url).func, adminDeleteChildFromClass) 


#	def test_guidUpdateView(self):
#	 	url = reverse('GuidUpdateView')
#	 	self.assertEquals(resolve(url).func, guidUpdateView) 	
	
	def test_tableReportGuide(self):
	 	url = reverse('tablereportGuide')
	 	self.assertEquals(resolve(url).func, tableReportGuide) 

	 	

	def test_HoursReportGuid(self):
	 	url = reverse('hoursReportGuid')
	 	self.assertEquals(resolve(url).func, HoursReportGuid)  	