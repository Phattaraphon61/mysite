# Generated by Django 3.0.3 on 2020-03-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_auto_20200318_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_select',
            name='problem_date_select',
            field=models.DateTimeField(),
        ),
    ]
