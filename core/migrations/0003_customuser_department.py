# Generated by Django 4.2.7 on 2023-11-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_customuser_date_of_birth_customuser_feedback_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]