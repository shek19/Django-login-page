from django import forms
from .models import *
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

class Registration(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    #gender = forms.ChoiceField(label="Gender", choices=User.GenderChoices.choices)
    age = forms.IntegerField(required=False)

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone_number', 'age']

    name = forms.CharField(
        label="Name", 
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )

    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'})
    )
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Phone number must be exactly 10 digits."
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    age = forms.IntegerField(
        label="Age",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'})
    )
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError('Name must contain only letters and spaces.')
        return name
 
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError('Phone number error')
        return phone
 
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 17 or age > 100:
            raise forms.ValidationError('Age must be between 17 and 100.')
        return age

class userSignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    
class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ('email', 'password')
