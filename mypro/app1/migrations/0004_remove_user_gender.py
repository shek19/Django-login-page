# Generated by Django 5.0.7 on 2024-08-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_user_age_alter_user_email_alter_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]