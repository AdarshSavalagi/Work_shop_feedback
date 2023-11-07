# Generated by Django 4.2.7 on 2023-11-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='customuser',
            name='feedback',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='quiz',
            field=models.JSONField(blank=True, null=True),
        ),
    ]