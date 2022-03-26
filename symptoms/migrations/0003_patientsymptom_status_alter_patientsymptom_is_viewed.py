# Generated by Django 4.0.2 on 2022-03-22 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0002_alter_patientsymptom_is_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsymptom',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patientsymptom',
            name='is_viewed',
            field=models.BooleanField(default=False),
        ),
    ]