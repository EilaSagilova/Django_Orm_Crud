# Generated by Django 5.0.4 on 2024-04-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hr", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="joined_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="employee",
            name="phone",
            field=models.IntegerField(null=True),
        ),
    ]
