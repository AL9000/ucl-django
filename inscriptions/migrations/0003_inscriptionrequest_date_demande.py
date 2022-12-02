# Generated by Django 4.1.3 on 2022-12-02 08:30

from django.db import migrations, models
import inscriptions.models


class Migration(migrations.Migration):

    dependencies = [
        ("inscriptions", "0002_academictraining_inscriptionrequest_trainings"),
    ]

    operations = [
        migrations.AddField(
            model_name="inscriptionrequest",
            name="date_demande",
            field=models.DateField(
                null=True, validators=[inscriptions.models.date_must_be_future]
            ),
        ),
    ]
