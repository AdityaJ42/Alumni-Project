from django.db import models
from django.urls import reverse

# Create your models here.
class Events(models.Model):
    event_name = models.CharField(max_length=50)
    day = models.DateField(null=True)
    location = models.TextField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('home')
