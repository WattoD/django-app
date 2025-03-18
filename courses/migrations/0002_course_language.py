# Generated by Django 5.1.7 on 2025-03-18 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='languages.language'),
        ),
    ]
