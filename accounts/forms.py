from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm,PasswordChangeForm
from . models import User

class UserRegister(UserCreationForm):
    password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:

        model = User
        fields = ['first_name','last_name','mobile','email','address','city']
        widgets = {
            'first_name': forms.TextInput(attrs={"type":"text","class":"form-control"}),
            'last_name': forms.TextInput(attrs={"type":"text","class":"form-control"}),
            'mobile': forms.TextInput(attrs={"type":"text","class":"form-control"}),
            'email': forms.TextInput(attrs={"type":"email","class":"form-control"}),
            'address': forms.TextInput(attrs={"type":"text-area","class":"form-control"}),
            'city': forms.TextInput(attrs={"type":"text","class":"form-control"}),
        }

class UserLogin(AuthenticationForm):
    
    class Meta:

        model = User
        fields = '__all__'
        
class PasswordReset(ModelForm):

    class Meta:

        model = User
        fields = ['password']
        widgets ={
            'password': forms.PasswordInput(attrs={'type':'password','class':'form-control'})
        }

class UserForm(ModelForm):

    class Meta:

        model = User
        fields = ['first_name','last_name','mobile','email','address','city']
        widgets = {
            'first_name': forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'mobile': forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'email': forms.TextInput(attrs={'type':'email','class':'form-control'}),
            'address': forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'city': forms.TextInput(attrs={'type':'text','class':'form-control'}),
        }