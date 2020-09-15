from django.db import models
from MyProfiles import settings
from django.contrib.auth.hashers import make_password

# Create your models here.
class Profiles(models.Model):
    social_media = models.CharField(max_length = 264)
    user_name = models.CharField(max_length = 264)

    def __str__():
        print("Contains list of all profiles that user has entered")