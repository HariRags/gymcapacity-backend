# Generated by Django 5.0.2 on 2024-03-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0005_alter_feedback_feedback_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='recently_deleted_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
