# Generated by Django 4.2.5 on 2023-10-04 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='assigned_to',
        ),
    ]
