from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile

class UserRegisterForm(UserCreationForm): #kayıt formu
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    bolum_name = forms.CharField(max_length = 30)
    fakulte_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2','bolum_name','fakulte_name']
    
class UserLoginForm(UserCreationForm): #giris formu
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email']

    
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username', 'email']
        

class ProfileUpdateForm(forms.ModelForm):
    #image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']

class FileUpdateForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model =Profile
        fields = ['file']


        