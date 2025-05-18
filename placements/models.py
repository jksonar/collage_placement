from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"{self.applicant_name} - {self.company.name}"

# Create your models here.
