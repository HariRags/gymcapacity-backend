# Generated by Django 5.0.2 on 2024-03-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0003_alter_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='roll',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
