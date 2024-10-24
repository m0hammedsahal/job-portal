from django.db import models

# Create your models here.
from django.db import models

from users.models import JobCreator
from django.urls import reverse

# A model for skill tags like 'React', 'Python', etc.
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)  # Optional company description
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)  # Optional logo upload

    industry = models.CharField(max_length=255)
    founded_year = models.IntegerField()
    employee_count = models.IntegerField()
    revenue = models.CharField(max_length=100)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class JobPosting(models.Model):
    # Employment types
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    EMPLOYMENT_TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
    ]
    
    job_creator = models.ForeignKey(JobCreator, on_delete=models.CASCADE)

    # Job basic info
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    
    # Job details
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()

    # Filters
    employment_type = models.CharField(max_length=2, choices=EMPLOYMENT_TYPE_CHOICES, default=FULL_TIME)
    is_remote = models.BooleanField(default=False)
    skills_required = models.ManyToManyField(Skill, blank=True)

    # Apply link and timestamps
    apply_link = models.URLField(max_length=500, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} at {self.company}'






class WorkerProfile(models.Model):
    job_creator = models.ForeignKey(JobCreator, on_delete=models.CASCADE)
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    # Education
    highest_education = models.CharField(max_length=255)  # e.g., Bachelor's, Master's, etc.
    institution_name = models.CharField(max_length=255)
    graduation_year = models.IntegerField()

    # Work Experience
    current_job_title = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    experience_years = models.IntegerField(default=0)

    # Skills
    skills = models.TextField(help_text="List of skills separated by commas")

    # Resume Upload
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    # Application Details
    applied_job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)  # Link to the job posting
    applied_at = models.DateTimeField(auto_now_add=True)

    interested = models.BooleanField(default=False)
    rejectd = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'




class Product(models.Model):
    # Your existing fields...
    
    def get_absolute_url(self):
        return reverse('web:product_detail', args=[str(self.id)])
