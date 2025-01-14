# Generated by Django 5.0.7 on 2024-08-11 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_user_email_user_gender_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(17, 'Age must be at least 17.'), django.core.validators.MaxValueValidator(100, 'Age cannot be more than 100.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator('Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[A-Za-z ]+$', 'Name must contain only letters and spaces.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Phone number must be exactly 10 digits.')]),
        ),
    ]
