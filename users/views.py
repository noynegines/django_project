from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserProfileForm , DeleteProfileForm , showGroupActiviesForm, addGroupActiviesForm
from users.models import UserProfile 
import json
#import requests

    #print(dataB)

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
        Ttable = UserProfile.objects.all()
        
        if deleteProfileForm.is_valid() :
            deleteProfileForm.given_id = deleteProfileForm.cleaned_data.get('given_id')
            all_tids = UserProfile.objects.values_list('t_id', flat=True).distinct()
            if(deleteProfileForm.given_id in all_tids):
                messages.success(request, f' succesfully deleted the guide !')
                instance = UserProfile.objects.get(t_id = deleteProfileForm.given_id).user
                instance.delete()

            else:
                messages.success(request, f' id doesnt exist !!!!!!!')   
            
            return render(request,'Admin1/homeAdmin.html')


    else:
        deleteProfileForm = DeleteProfileForm()
        Ttable=UserProfile.objects.all()
    

    context = { 'deleteProfileForm' : deleteProfileForm ,'Ttable': Ttable}
    return render(request,'Admin1/deleteTeacher.html',context)    




def GroupActivitiesTable(request):

    
    x = []
    inX = []
    with open('users/classes.json' , encoding="utf8" ) as db:
        Ttable=json.load(db)  

    #for d in Ttable:
    #    d["guide"]=''

    #with open('users/Newclasses.json' , encoding="utf8" ) as ty :
    #    Ttable=json.load(db)    


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
                    #inX.append(row["guide"])
                    x.append(inX)
                    inX=[]

        else:
            messages.success(request, f' not valid form !') 

        context = { 'ShowGroupActiviesForm' : ShowGroupActiviesForm , 'Ttable': Ttable , 'x' : x }      
        #print(x )
        return render(request,'simpleuser/GroupActivitiesTable.html',context)


    else:
        ShowGroupActiviesForm = showGroupActiviesForm()
        #AddActivitiesGroup
    
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
            for item in Ttable:
                if ( item["class-name"].replace(' ', '')== given_groupActivity.replace(' ', '') and item["neighborhood"].replace(' ', '') == y[2].replace(' ', '') and item["phone"].replace(' ', '') == y[1].replace(' ', '') and item["location"].replace(' ', '') == y[0].replace(' ', '') and item["min-age"].replace(' ', '') == minAge and item["max-age"].replace(' ', '') == maxAge ):
                    messages.warning(request, f' group activity already exist  !')
                    return render(request, 'Admin1/AddActivitiesGroup.html', context)

            newl={"location": " ", "phone": " ", "neighborhood": " ", "category": " ", "subcategory": " ", "class-name": " ", "min-age": "", "max-age": "", "audience": " ","guide":" "}
            newl["location"]=y[0]
            newl["phone"]=y[1]
            newl["neighborhood"]=y[2]
            newl["class-name"]=given_groupActivity
            newl["min-age"]=minAge
            newl["max-age"]=maxAge
            newl["guide"]=teacherID
            #print(newl)
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


def registerToClass(request):
    return render(request, 'simpleuser/registerToClass.html')

def showMyClasses(request):
    return render(request, 'simpleuser/showMyClasses.html')

def TeacherDetail(request):
    return render(request, 'simpleuser/TeacherDetail.html')

def childrenList(request):
    return render(request, 'guide/childrenList.html')

def editDetails(request):
    return render(request, 'guide/editDetails.html')

def ShowMyClass(request):
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