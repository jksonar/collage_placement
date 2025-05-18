# User Models (accounts/models.py)
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
    placement_status = models.CharField(max_length=20)

# Placement Models (placements/models.py)
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
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    applied_date = models.DateTimeField(auto_now_add=True)
    offer_letter = models.FileField(upload_to='offer_letters/', null=True, blank=True)

class OffCampusApplication(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    applied_date = models.DateTimeField(auto_now_add=True)