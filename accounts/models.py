from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_type = models.CharField(max_length=20, choices=[
        ('student', 'Student'),
        ('placement_admin', 'Placement Admin'),
        ('college_admin', 'College Admin')
    ])

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    placement_status = models.CharField(max_length=20, choices=[
        ('unplaced', 'Unplaced'),
        ('placed', 'Placed'),
        ('placed_twice', 'Placed Twice')
    ], default='unplaced')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.course} - {self.branch}"

# Create your models here.
