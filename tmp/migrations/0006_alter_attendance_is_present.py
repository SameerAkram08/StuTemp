# Generated by Django 4.2.6 on 2023-10-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0005_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='is_present',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=7),
        ),
    ]
