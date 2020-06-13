





from django.test import TestCase
from users.models import HoursReport, RegisterChild, UserProfile
from django.contrib.auth.models import User

# models test
class modelsTest(TestCase):


    def create_HoursReport(self, t_id="123456789", start_hour="01:00" , finish_hour="02:00" , date="2020-06-08"):
        return HoursReport.objects.create(t_id=t_id, start_hour=start_hour, finish_hour=finish_hour , date=date)

    def test_HoursReport_creation(self):
        w = self.create_HoursReport()
        self.assertTrue(isinstance(w, HoursReport))
        self.assertEqual(w.__str__(), w.t_id + w.start_hour + w.finish_hour + w.date)


    def create_RegisterChild(self, ID_P="17", ID_C="222222223" , FName_C="romi" , LName_C="alma" , Age_C="7" , Phone_P="0525676981" ,idClass="68" ):
        return RegisterChild.objects.create(ID_P=ID_P, ID_C=ID_C, FName_C=FName_C , LName_C=LName_C , Age_C=Age_C , Phone_P=Phone_P , idClass=idClass )
    
    def test_RegisterChild_creation(self):
        w = self.create_RegisterChild()
        self.assertTrue(isinstance(w, RegisterChild))
        self.assertEqual(w.__str__(),w.ID_P + w.ID_C +w.FName_C+w.LName_C+w.Age_C+w.Phone_P+w.idClass)

    def create_UserProfile(self, user, phone="0525676981", t_id="romi", aboutMe="alma"):
        return UserProfile.objects.create(user=user, phone=phone, t_id=t_id, aboutMe=aboutMe)

    def test_UserProfile_creation(self):
        self.user_login = {'username': 'tempTest','password': 'test1111'}
        self.user = User.objects.create_user(**self.user_login)
        self.user.save()

        w = self.create_UserProfile(self.user)
        self.assertTrue(isinstance(w, UserProfile))
        self.assertEqual(w.__str__(), w.user.username+w.phone+w.t_id+w.aboutMe)
