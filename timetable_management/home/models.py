from django.db import models

# Create your models here.python manage.py makemigrations
class Teacher(models.Model):
    t_name = models.CharField(max_length=100)
    t_id = models.IntegerField(max_length=20)
class courses(models.Model):
    branch_name = models.CharField(max_length=100)
    
