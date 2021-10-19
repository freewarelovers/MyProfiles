from django.db import models
from MyProfiles import settings
from django.contrib.auth.hashers import make_password

# Create your models here.
class Profile(models.Model):
    '''Profile data table handles the username and passwords of other websites for each respective user'''
    user_id = models.ForeignKey(models.LogIn, on_delete = models.CASCADE)
    social_media = models.CharField(max_length = 264, null = True)
    user_name = models.CharField(max_length = 264, null = True)
    password = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return self.name

class LogIn(models.Model):
    '''LogIn data table consists of user name and password to login to the MyProfiles portal'''
    user_name = models.CharField(max_length = 264, unique = True)
    password = models.CharField(max_length = 1000, null = True) 

    def __str__(self):
        return self.name