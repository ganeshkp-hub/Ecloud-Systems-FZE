from django.db import models

# Create your models here.

class UsersDetails(models.Model):


    User_Id = models.IntegerField(primary_key=True)
    User_Name = models.CharField(max_length=20)
    User_Password = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

