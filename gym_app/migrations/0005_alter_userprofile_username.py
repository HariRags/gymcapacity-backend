# Generated by Django 5.0.2 on 2024-03-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0004_alter_userprofile_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]