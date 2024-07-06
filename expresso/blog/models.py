from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Blog(models.Model):
    JOB_TYPE = (
        ('FT','Full Time'),
        ('PT','Part Time'),
        ('INTERN','Internship'),
    )
    USER_TYPE = (
        ('STUD','Student'),
        ('PROF','Professional'),
    )
    JOB_ROLE = (
        ('DEV','Developer'),
        ('DES','Designer'),
        ('MKT','Marketing'),
    )
    BLOG_TYPE = (
        ('INTERVIEW','Interview'),
        ('WORK EXP','Work Experience'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/",blank=True,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_type = models.CharField(max_length=6,choices=JOB_TYPE)
    user_type = models.CharField(max_length=4,choices=USER_TYPE)
    job_role = models.CharField(max_length=3,choices=JOB_ROLE)
    blog_type = models.CharField(max_length=10,choices=BLOG_TYPE)
    organization = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.user.username}-{self.organization}-{self.job_role}'
