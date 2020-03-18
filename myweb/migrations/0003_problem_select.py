# Generated by Django 3.0.3 on 2020-03-18 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='problem_select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=50)),
                ('username_select', models.CharField(max_length=50)),
                ('problem_date_select', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]