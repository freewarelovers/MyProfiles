from django.db import models
from MyProfiles import settings
from django.contrib.auth.hashers import make_password

class User(models.Model):
    user_name = models.CharField(max_length = 264, null = False)
    password = models.CharField(max_length = 32, null = False)

class Profile(models.Model):
    '''Profile data table handles the username and passwords of other websites for each respective user'''
    social_media = models.CharField(max_length = 264, null = True)
    user_name = models.CharField(max_length = 264, null = True)
    password = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return self.name