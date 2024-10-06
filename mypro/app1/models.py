from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator, MinLengthValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
class User(models.Model):
    
    name = models.CharField(max_length=100, validators=[
        RegexValidator(r'^[A-Za-z ]+$', 'Name must contain only letters and spaces.')
    ])
    email = models.EmailField(unique=True, validators=[
        EmailValidator('Enter a valid email address.')
    ])
    

    age = models.PositiveIntegerField(validators=[
        MinValueValidator(17, 'Age must be at least 17.'),
        MaxValueValidator(100, 'Age cannot be more than 100.')
    ])
    
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])

    
    phone_number = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{10}$', 'Phone number must be exactly 10 digits.')
    ])
    
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name
