from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')

    class Meta:
        model = User
        fields = ['username' ,'first_name','last_name', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    
    t_id = forms.CharField(max_length=9, min_length=9,widget=forms.TextInput(attrs={'type':'number','min':'0'}))
    phone = forms.CharField(max_length=10, min_length=10,widget=forms.TextInput(attrs={'type':'number','min':'0'}))
	
    class Meta:
        model = UserProfile
        fields = [ 'phone' , 't_id' ]



class DeleteProfileForm(forms.ModelForm):
    
    given_id = forms.CharField( max_length=9, min_length=9,widget=forms.TextInput(attrs={'type':'number','min':'0'}),label='the id of the teacher you want to delete : ')
    
    class Meta:
        model = UserProfile
        fields = [ 'given_id' ]


class showGroupActiviesForm(forms.ModelForm):
    
    age = forms.CharField( max_length=2, min_length=1,widget=forms.TextInput(attrs={'type':'number','min':'0'}),label='kid age:')
    CHOICES= (
        ("שכונה ט'", "שכונה ט"),
        ("שכונת רמות ", "שכונת רמות "),
        ("שכונת דרום ", "שכונת דרום "),
        ("שכונה ד' ", "שכונה ד"),
        ("שכונת נאות לון ", "שכונת נאות לון "),
        ("שכונת נווה נוי ", "שכונת נווה נוי "),
        ("שכונת נווה זאב ", "שכונת נווה זאב "),
        ("שכונה ה' ", "שכונה ה"),

    )
    select = forms.CharField(widget=forms.Select(choices=CHOICES))

    class Meta:
        model = User
        fields = [ 'age'  ]




class addGroupActiviesForm(forms.ModelForm):
    CHOICES = (
        ( "אשכול פיס,08-6434775,שכונה ט'","location: אשכול פיס ,neighborhood:שכונה ט "),
        (" מתנ\"ס רמות ספורטיב,08-6414444,שכונת רמות ","location: מתנ\"ס רמות ספורטיב ,neighborhood: שכונת רמות"),
        ( "אשכול רמות ,08-6414444,שכונת רמות ","location: אשכול רמות  ,neighborhood: שכונת רמות"),
        ( "הרוח היהודית  ,08-6290060,שכונת רמות ","location:הרוח היהודית  ,neighborhood:שכונת דרום"),
        ( "פאני קפלן  ,08-6487614,שכונה ד","location: פאני קפלן   ,neighborhood: שכונה ד"),
        ("מרגליות ,08-6230422,שכונת דרום ","location:מרגליות ,neighborhood: שכונת דרום "),
        ( "נאות לון,08-6226920,שכונת נאות לון ","location:נאות לון     ,neighborhood: שכונת נאות לון'"),
        ( "נווה נוי ,08-6226922,שכונת נווה נוי ","location:נווה נוי    ,neighborhood: שכונת נווה נוי'",),
        ("רמב\"ם ,054-7395076,שכונה ה' ","location:רמב\"ם    ,neighborhood:שכונה ה"),
        ("אולם ספורט נווה נוי/מענית  ,08-6226922,שכונת נווה נוי ","location:אולם ספורט נווה נוי/מענית   ,neighborhood: שכונת נווה נוי"),
        ( "נווה זאב ,08-6226909,שכונת נווה זאב ","location:נווה זאב  ,neighborhood:שכונת נווה זאב '"),
        ( "קתדרה ,08-6414444,שכונת רמות ","location:קתדרה    ,neighborhood: שכונת רמות'"),
        ( "דניס הישרדות ,08-6433388,שכונה ד","location:דניס הישרדות    ,neighborhood:שכונה ד'"),
        ("מועדון השחמט העירוני ,08-6277421,שכונה ב'","location:מועדון השחמט העירוני  ,neighborhood: שכונת רמותשכונה ב'"),
        ("מתנ\"ס יא ,08-6433388,שכונה י\"א ","location:מתנ\"ס יא  ,neighborhood: שכונה י\"א ת'"),
        ("רגר   ,08-6109638,שכונת נווה זאב ","location:רגר    ,neighborhood: שכונת נווה זאב '",)
    )
    select = forms.CharField(widget=forms.Select(choices=CHOICES))
    ageMax = forms.CharField(max_length=2, min_length=1, widget=forms.TextInput(attrs={'type': 'number', 'min': '0'}),label='max age:')
    ageMin = forms.CharField(max_length=2, min_length=1, widget=forms.TextInput(attrs={'type': 'number', 'min': '0'}),label='min age:')
    nameClas= forms.CharField(max_length=30, label='class name')
    given_id = forms.CharField( max_length=9, min_length=9,widget=forms.TextInput(attrs={'type':'number','min':'0'}),label='the id of the teacher: ')


    class Meta:
        model = User
        fields = ['ageMax','ageMin' ,'nameClas' , 'given_id']
