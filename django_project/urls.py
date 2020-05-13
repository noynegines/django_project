"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login1/', user_views.login1, name='login1'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('registerTeacher/', user_views.profile, name='registerTeacher'),
    path('deleteTeacher/', user_views.DeleteTeacher, name='deleteTeacher'),
    path('TeacherTable/',user_views.TeacherTable,name ='TeacherTable'),
    path('groupActivityTable/',user_views.GroupActivitiesTable,name ='groupActivityTable'),
    path('AdminGroupActivityTable/',user_views.AdminGroupActivitiesTable,name ='AdminGroupActivityTable'),
    path('AddActivitiesGroup/',user_views.AddActivitiesGroup,name ='AddActivitiesGroup'),
    path('', include('homepage.urls')),
    path('registerToClass/',user_views.registerToClass, name='registerToClass'),
    path('showMyClasses/',user_views.showMyClasses, name='showMyClasses'),
    path('TeacherDetail/',user_views.TeacherDetail, name='TeacherDetail'),
    path('childrenList/', user_views.childrenList, name='childrenList'),
    path('editDetails/', user_views.editDetails, name='editDetails'),
    path('ShowMyClass/', user_views.ShowMyClass, name='ShowMyClass'),


]
