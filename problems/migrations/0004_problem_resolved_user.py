# Generated by Django 4.2.5 on 2023-10-04 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0003_remove_problem_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='resolved_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resolved_problems', to=settings.AUTH_USER_MODEL),
        ),
    ]
