from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fisrtname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class problem(models.Model):
    problem_name = models.CharField(max_length=200)

    def __str__(self):
        return self.problem_name

class problem_select(models.Model):
    problem_name = models.CharField(max_length=50)
    username_select = models.CharField(max_length=50)
    problem_date_select = models.DateField()

    def __str__(self):
        return (f'{self.problem_date_select}')


    
