from django.db import models
from django.conf import settings

# class Company(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     location = models.CharField(max_length=255)
#     website = models.URLField()

#     def __str__(self):
#         return self.name

# class JobApplication(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     applicant_name = models.CharField(max_length=255)
#     application_date = models.DateField(auto_now_add=True)
#     status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')])

#     def __str__(self):
#         return f"{self.applicant_name} - {self.company.name}"

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=[
        ('mass', 'Mass'),
        ('core', 'Core'),
        ('dream', 'Dream')
    ])
    description = models.TextField()
    eligibility_criteria = models.TextField()
    job_description = models.TextField()
    application_deadline = models.DateField()

class JobApplication(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    applied_date = models.DateTimeField(auto_now_add=True)
    offer_letter = models.FileField(upload_to='offer_letters/', null=True, blank=True)

# class OffCampusApplication(models.Model):
#     student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=200)
#     role = models.CharField(max_length=100)
#     status = models.CharField(max_length=20)
#     applied_date = models.DateTimeField(auto_now_add=True)