from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    department = models.CharField(max_length=40)
    year_of_graduation = models.CharField(max_length=4)
    profile_pic = models.FileField(upload_to='profile pics/')
    profession = models.TextField(max_length=100)

    def __str__(self):
        return self.name
