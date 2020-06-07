from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserProfileForm , DeleteProfileForm , showGroupActiviesForm, addGroupActiviesForm,registerToClassForm , adminMatnasForm  , adminDeleteClassForm , adminEditClassForm , guideClassRegistersForm,adminDeleteChildFromClassForm
from users.models import UserProfile , RegisterChild
import json
from django.views.generic import (
    UpdateView

)
from django import forms
#import requests

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.first_name = form.cleaned_data.get('first_name')
            form.last_name = form.cleaned_data.get('last_name')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('homepage-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login1(request):
    if request.user.is_superuser == 1:
        return render(request,'Admin1/homeAdmin.html')
    if request.user.is_superuser == 0:
        if request.user.is_staff == 0:
            return render(request, 'simpleuser/homeSimpleuser.html')
        if request.user.is_staff == 1:  
            return render(request, 'guide/homeGuide.html')

def profile(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)


        if form.is_valid() and profile_form.is_valid():
            form.first_name = form.cleaned_data.get('first_name')
            form.last_name = form.cleaned_data.get('last_name')
            user = form.save()
            user.is_staff = 1
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request,'Admin1/homeAdmin.html')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    context = { 'form' : form , 'profile_form' : profile_form }     
    return render(request, 'Admin1/registerTeacher.html', context )



def TeacherTable(request):
    Ttable=UserProfile.objects.all()
    context = {'Ttable': Ttable}
    return render(request,'Admin1/TeacherTable.html',context)


def DeleteTeacher(request):
    if request.method == 'POST':
        deleteProfileForm = DeleteProfileForm(request.POST)
        context = {'deleteProfileForm': deleteProfileForm}
        if deleteProfileForm.is_valid():
            deleteProfileForm.given_id = deleteProfileForm.cleaned_data.get('given_id')
            all_tids = UserProfile.objects.values_list('t_id', flat=True).distinct()
            if (deleteProfileForm.given_id in all_tids):
                with open('users/classes.json', encoding="utf8") as db:
                    Ttable = json.load(db)
                for item in Ttable:
                    if (item["guide"] == deleteProfileForm.given_id):
                        item["guide"] = " "
                with open('users/classes.json', 'w', encoding="utf8") as newF:
                    json.dump(Ttable, newF, indent=1)
                instance = UserProfile.objects.get(t_id=deleteProfileForm.given_id).user
                instance.delete()
                messages.success(request, f' succesfully deleted the guide !')
                return render(request, 'Admin1/homeAdmin.html')

            else:
                messages.warning(request, f' id doesnt exist !!!!!!!')
                return render(request, 'Admin1/deleteTeacher.html', context)
    else:
        deleteProfileForm = DeleteProfileForm()
        Ttable = UserProfile.objects.all()
        context = {'deleteProfileForm': deleteProfileForm}
    return render(request, 'Admin1/deleteTeacher.html', context)



def GroupActivitiesTable(request):

    
    x = []
    inX = []
    with open('users/classes.json' , encoding="utf8" ) as db:
        Ttable=json.load(db)
    if request.method == 'POST':
        ShowGroupActiviesForm = showGroupActiviesForm(request.POST)
        if ShowGroupActiviesForm.is_valid() :

            y = ShowGroupActiviesForm.cleaned_data.get('select') 
            ShowGroupActiviesForm.age = ShowGroupActiviesForm.cleaned_data.get('age')
            ShowGroupActiviesForm.neighborhood = ShowGroupActiviesForm.cleaned_data.get('neighborhood')
            for row in Ttable:
                if(  row["neighborhood"] .replace(' ','')==y.replace(' ','')  and ( row["min-age"]=="" or int(row["min-age"]) <=  int(ShowGroupActiviesForm.age)) and (row["max-age"]=="" or int(row["max-age"]) >= int(ShowGroupActiviesForm.age)) ):
                    inX.append(row["location"])
                    inX.append(row["phone"])
                    inX.append(row["neighborhood"])
                    inX.append(row["class-name"])
                    inX.append(row["min-age"])
                    inX.append(row["max-age"])
                    inX.append(row["idC"])
                    x.append(inX)
                    inX=[]

        else:
            messages.success(request, f' not valid form !') 

        context = { 'ShowGroupActiviesForm' : ShowGroupActiviesForm , 'Ttable': Ttable , 'x' : x }
        return render(request,'simpleuser/GroupActivitiesTable.html',context)


    else:
        ShowGroupActiviesForm = showGroupActiviesForm()
    
    context = { 'ShowGroupActiviesForm' : ShowGroupActiviesForm , 'Ttable': Ttable , 'x' : x }
    return render(request,'simpleuser/GroupActivitiesTable.html',context )


def AddActivitiesGroup(request):
    if request.method == 'POST':
        AddGroupActiviesForm = addGroupActiviesForm(request.POST)

        if AddGroupActiviesForm.is_valid():
            context = {'AddGroupActiviesForm': AddGroupActiviesForm}
            maxAge = AddGroupActiviesForm.cleaned_data.get('ageMax')
            minAge = AddGroupActiviesForm.cleaned_data.get('ageMin')
            if (int(maxAge) - int(minAge) < 0):
                messages.warning(request, f' min age is bigger than max age !')
                return render(request, 'Admin1/AddActivitiesGroup.html', context)
            teacherID = AddGroupActiviesForm.cleaned_data.get('given_id')
            all_tids = UserProfile.objects.values_list('t_id', flat=True).distinct()
            if (teacherID not in all_tids):
                messages.warning(request, f' there is no guide with this id  !')
                return render(request, 'Admin1/AddActivitiesGroup.html', context)
            given_groupActivity = AddGroupActiviesForm.cleaned_data.get('nameClas')
            y = AddGroupActiviesForm.cleaned_data.get('select')
            y = y.split(',')
            groupActivityList = []
            with open('users/classes.json', encoding="utf8") as db:
                Ttable = json.load(db)
            i=0
            for item in Ttable:
                if i<item["idC"]:
                    i=item["idC"]
                if ( item["class-name"].replace(' ', '')== given_groupActivity.replace(' ', '') and item["neighborhood"].replace(' ', '') == y[2].replace(' ', '') and item["phone"].replace(' ', '') == y[1].replace(' ', '') and item["location"].replace(' ', '') == y[0].replace(' ', '') and item["min-age"].replace(' ', '') == minAge and item["max-age"].replace(' ', '') == maxAge ):
                    messages.warning(request, f' group activity already exist  !')
                    return render(request, 'Admin1/AddActivitiesGroup.html', context)
            i=i+1
            newl={"location": " ", "phone": " ", "neighborhood": " ", "category": " ", "subcategory": " ", "class-name": " ", "min-age": "", "max-age": "", "audience": " ","guide":" ","idC":0}
            newl["location"]=y[0]
            newl["phone"]=y[1]
            newl["neighborhood"]=y[2]
            newl["class-name"]=given_groupActivity
            newl["min-age"]=minAge
            newl["max-age"]=maxAge
            newl["guide"]=teacherID
            newl["idC"] = i
            Ttable.append(newl)
            with open('users/classes.json', 'w' , encoding="utf8") as newF:
                json.dump(Ttable , newF , indent = 1)


            messages.success(request, f' added succesfully the group activity !')
            return render(request, 'Admin1/homeAdmin.html', context)

    else:
        AddGroupActiviesForm = addGroupActiviesForm()

    context = {'AddGroupActiviesForm': AddGroupActiviesForm}
    return render(request, 'Admin1/AddActivitiesGroup.html', context)



def AdminGroupActivitiesTable(request):
    x = []
    inX = []
    with open('users/classes.json' , encoding="utf8" ) as db:
        Ttable=json.load(db)  

    for row in Ttable:

        inX.append(row["location"])
        inX.append(row["phone"])
        inX.append(row["neighborhood"])
        inX.append(row["class-name"])
        inX.append(row["min-age"])
        inX.append(row["max-age"])
        inX.append(row["guide"])
        x.append(inX)
        inX=[]

    context = { 'Ttable': Ttable , 'x' : x }
    return render(request,'Admin1/showGroupActivies.html',context )


def adminShowRegisters(request):
    x = []
    inX = []

    value = RegisterChild.objects.all()
    for item in value:
        inX.append(item.ID_P)
        inX.append(item.ID_C)
        inX.append(item.FName_C)
        inX.append(item.LName_C)
        inX.append(item.Age_C)
        inX.append(item.Phone_P)
        inX.append(item.idClass)
        x.append(inX)
        inX = []

    context = {'x': x}
    return render(request, 'Admin1/showRegisters.html', context)

def registerToClass(request):
    if request.method == 'POST':
        RegisterToClassForm = registerToClassForm(request.POST)

        if RegisterToClassForm.is_valid():
            context = {'RegisterToClassForm': RegisterToClassForm}
            ID_P = request.user.id
            ID_C = RegisterToClassForm.cleaned_data.get('ID_C')
            FName_C = RegisterToClassForm.cleaned_data.get('FName_C')
            LName_C = RegisterToClassForm.cleaned_data.get('LName_C')
            Age_C = RegisterToClassForm.cleaned_data.get('Age_C')
            Phone_P = RegisterToClassForm.cleaned_data.get('Phone_P')
            IDclass = RegisterToClassForm.cleaned_data.get('select')
            #RegisterToClassForm.save()
            t = RegisterChild.objects.all()

            for item in t:
                if item.ID_C == ID_C and (item.FName_C != FName_C or item.LName_C != LName_C):
                    messages.warning(request, f'your id is already exist whit other name')
                    return render(request, 'simpleuser/registerToClass.html', context)

                if item.ID_C == ID_C and item.idClass == IDclass :
                    messages.warning(request, f'you are already sign to this class')
                    return render(request, 'simpleuser/registerToClass.html', context)

                with open('users/classes.json', encoding="utf8") as db:
                    MyClass = json.load(db)

                for row in MyClass:
                    if row["idC"] == int(IDclass) :
                        minA =row["min-age"]
                        maxA = row["max-age"]
                        print(type( maxA))
                        print(minA,minA)
                        if  int(Age_C) > int(maxA) or int(Age_C) < int(minA) :
                            messages.warning(request, f'your age is not in the range')
                            return render(request, 'simpleuser/registerToClass.html', context)

            rc = RegisterChild(ID_P=ID_P , ID_C=ID_C , FName_C = FName_C , LName_C = LName_C , Age_C = Age_C ,
            Phone_P = Phone_P , idClass = IDclass )
            rc.save()
            messages.success(request, f' The registration for the class was successful !')
            return render(request, 'simpleuser/homeSimpleuser.html',context)
        
    else:
        RegisterToClassForm = registerToClassForm()


    context = {'RegisterToClassForm': RegisterToClassForm }
    return render(request, 'simpleuser/registerToClass.html', context)


def showMyClasses(request): #לקוח
    x = []
    inX = []
    tid = request.user.id
    
    value = RegisterChild.objects.all()

    with open('users/classes.json' , encoding="utf8" ) as db:
        MyClass=json.load(db)

    for item in value:
        if int(tid) == int(item.ID_P):
            for t in MyClass:
                if int(t["idC"]) == int(item.idClass):
                    inX.append(item.ID_C)
                    inX.append(item.FName_C)
                    inX.append(item.LName_C)
                    inX.append(item.Age_C)
                    inX.append(item.Phone_P)
                    inX.append(t["location"])
                    inX.append(t["class-name"])
                    nameG="";
                    if t["guide"]!=" ":
                        instance = UserProfile.objects.get(t_id=t["guide"])
                        nameG=instance.user.first_name+ " "+instance.user.last_name
                    inX.append(nameG)
                    x.append(inX)
                    inX = []

    context = {'x': x}
    return render(request, 'simpleuser/showMyClasses.html',context)


def editDetails(request):
    return render(request, 'guide/editDetails.html')

def ShowMyClass(request): #מדריך
    tid = request.user.userprofile.t_id
    x = []
    inX = []
    with open('users/classes.json' , encoding="utf8" ) as db:
        MyClass=json.load(db)

    for row in MyClass:
        if tid == row["guide"]:
            inX.append(row["location"])
            inX.append(row["phone"])
            inX.append(row["neighborhood"])
            inX.append(row["class-name"])
            inX.append(row["min-age"])
            inX.append(row["max-age"])
            inX.append(row["guide"])
            x.append(inX)
            inX=[]

    context = { 'MyClass': MyClass , 'x' : x }
    return render(request,'guide/ShowMyClass.html',context )


def adminShowRegistersByMatnas(request):
    if request.method == 'POST':
        AdminMatnasForm = adminMatnasForm(request.POST)
        x = []
        inX = []

        with open('users/classes.json', encoding="utf8") as db:
            Ttable = json.load(db)

        value = RegisterChild.objects.all()
        if AdminMatnasForm.is_valid():
            matnas = AdminMatnasForm.cleaned_data.get('select')
            for item in value:
                RegisterClassId = item.idClass
                for row in Ttable:
                    if (int(row["idC"]) == int(RegisterClassId)):
                        if (row["location"].replace(' ', '') == matnas.replace(' ', '')):
                            inX.append(item.ID_P)
                            inX.append(item.ID_C)
                            inX.append(item.FName_C)
                            inX.append(item.LName_C)
                            inX.append(item.Age_C)
                            inX.append(item.Phone_P)
                            inX.append(item.idClass)
                            x.append(inX)
                            inX = []

            context = {'x': x, 'AdminMatnasForm': AdminMatnasForm}

    else:
        AdminMatnasForm = adminMatnasForm()
        context = {'AdminMatnasForm': AdminMatnasForm}

    return render(request, 'Admin1/showRegistersByMatnas.html', context)



def Admin_Delete_Class(request):
    if request.method == 'POST':
        print("spir")
        AdminDeleteClassForm = adminDeleteClassForm(request.POST)
        if AdminDeleteClassForm.is_valid():
            IDclass = AdminDeleteClassForm.cleaned_data.get('select')
            with open('users/classes.json', encoding="utf8") as db:
                Ttable = json.load(db)    
            
            for item in Ttable:
    
                if item["idC"] == int(IDclass):
                    Ttable.remove(item)
                    with open('users/classes.json', 'w' , encoding="utf8") as newF:
                        json.dump(Ttable , newF , indent = 1)
                    messages.success(request, f'deleted successfully !')
                    break

            value = RegisterChild.objects.all()
            for child in value:
                if int(child.idClass) == int(IDclass):
                    child.delete()
        return render(request, 'Admin1/homeAdmin.html')
    else:
        print("adva")
        AdminDeleteClassForm = adminDeleteClassForm()
        print("zzzzzzzzzzzz")
    context = {'AdminDeleteClassForm': AdminDeleteClassForm}
    return render(request, 'Admin1/DeleteClass.html', context)



def Admin_Edit_Class(request):
    if request.method == 'POST':
        AdminEditClassForm = adminEditClassForm(request.POST)
        if AdminEditClassForm.is_valid():
            GuideId = AdminEditClassForm.cleaned_data.get('Guide')
            ClassId = AdminEditClassForm.cleaned_data.get('Class')
         
            with open('users/classes.json', encoding="utf8") as db:
                Ttable = json.load(db)    
            
            for item in Ttable:
    
                if item["idC"] == int(ClassId):
                    
                    item["guide"] = GuideId
                    with open('users/classes.json', 'w' , encoding="utf8") as newF:
                        json.dump(Ttable , newF , indent = 1)
                    break
                    
        messages.success(request, f'edited successfully !')  
        return render(request, 'Admin1/homeAdmin.html')           

            
    else:
        AdminEditClassForm = adminEditClassForm()
        
    context = {'AdminEditClassForm': AdminEditClassForm}
    return render(request, 'Admin1/editActivityG.html', context)




def GuideShowRegistersByClass(request):
    x = []
    inX = []
    if request.method == 'POST':
        GuideClassRegistersForm = guideClassRegistersForm(request.user.userprofile.t_id,request.POST)
        value = RegisterChild.objects.all()
        if GuideClassRegistersForm.is_valid():
            classId = GuideClassRegistersForm.cleaned_data.get('select')

            for item in value:
                RegisterClassId = item.idClass#.replace(' ', '')

                if (int(classId) == int(RegisterClassId)):
                    inX.append(item.ID_P)
                    inX.append(item.ID_C)
                    inX.append(item.FName_C)
                    inX.append(item.LName_C)
                    inX.append(item.Age_C)
                    inX.append(item.Phone_P)
                    inX.append(item.idClass)
                    x.append(inX)
                    inX = []
        context = {'x': x , 'GuideClassRegistersForm': GuideClassRegistersForm}
        return render(request, 'guide/guideClassRegisters.html', context)
    else:
        GuideClassRegistersForm = guideClassRegistersForm(request.user.userprofile.t_id)
        context = {'x':x,'GuideClassRegistersForm': GuideClassRegistersForm}
    
    return render(request, 'guide/guideClassRegisters.html', context)
def simpleuserDetailGuideS(request):
    x = []
    inX = []
    tid = request.user.id

    value = RegisterChild.objects.all()

    with open('users/classes.json', encoding="utf8") as db:
        MyClass = json.load(db)

    for item in value:
        if int(tid) == int(item.ID_P):
            for t in MyClass:
                if int(t["idC"]) == int(item.idClass):
                    nameG = "";
                    DidelG=""
                    if t["guide"] != " ":
                        instance = UserProfile.objects.get(t_id=t["guide"])
                        nameG = instance.user.first_name + " " + instance.user.last_name
                        DidelG=instance.aboutMe
                        if nameG not in  inX:
                            inX.append(nameG)
                            inX.append(DidelG)

    context = {'inX': inX}
    return render(request, 'simpleuser/simpDetailGuideS.html', context)


def adminDeleteChildFromClass(request):
    if request.method == 'POST':
        AdminDeleteChildFromClassForm = adminDeleteChildFromClassForm(request.POST)
        context = {'AdminDeleteChildFromClassForm': AdminDeleteChildFromClassForm}
        if AdminDeleteChildFromClassForm.is_valid():
            y = AdminDeleteChildFromClassForm.cleaned_data.get('class')
            y = y.split(',')
            IDC = AdminDeleteChildFromClassForm.cleaned_data.get('ID_C')
            print(type(IDC))

            q1 = RegisterChild.objects.filter(idClass=y[0])
            q1 = RegisterChild.objects.filter(ID_C=IDC)
            q1.delete()
            messages.success(request, f' succesfully deleted child from class !')
            # value = RegisterChild.objects.all()
    else:
        AdminDeleteChildFromClassForm = adminDeleteChildFromClassForm()
        context = {'AdminDeleteChildFromClassForm': AdminDeleteChildFromClassForm}
    return render(request,'Admin1/adminDeleteChildFromClass.html', context)

class guidUpdateView(UpdateView):
    model = UserProfile
    template_name = 'guide/editDetails.html'
    fields = ['aboutMe']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


