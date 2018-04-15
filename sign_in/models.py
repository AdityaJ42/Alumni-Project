from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    year_of_graduation = models.CharField(max_length=4)
    profile_pic = models.FileField(upload_to='profile pics/', default='user.png')
    profession = models.TextField(max_length=100)

    DEPT = (('Computer Engineering', 'Computer Engineering'),
            ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
            ('Electronics Engineering', 'Electronics Engineering'),
            ('Chemical Engineering', 'Chemical Engineering'),
            ('Mechanical Engineering', 'Mechanical Engineering'),
            ('Production Engineering', 'Production Engineering'),
            ('Biomedical Engineering', 'Biomedical Engineering'),
            ('Information Technology', 'Information Technology'),)

    department = models.CharField(max_length=50, choices=DEPT, default='--------')

    def __str__(self):
        return self.name
