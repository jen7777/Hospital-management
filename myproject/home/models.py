from django.db import models

# database , always migrate in terminal and register in admin.py

class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

