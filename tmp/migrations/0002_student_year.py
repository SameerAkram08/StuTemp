# Generated by Django 4.2.6 on 2023-10-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.PositiveIntegerField(default=2023),
        ),
    ]
