# Generated by Django 4.2.6 on 2023-10-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmp', '0002_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='RollNo',
            field=models.CharField(default='Fa-', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=4),
        ),
    ]
