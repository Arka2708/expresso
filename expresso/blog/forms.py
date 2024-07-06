from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'photo', 'content', 'job_type', 'user_type', 'job_role', 'blog_type', 'organization']
        labels = {
            'title': 'Title',
            'photo': 'Feature Image',
            'content': 'Blog Content',
            'job_type': 'Type of Job',
            'user_type': 'Category',
            'job_role': 'Job Role',
            'blog_type': 'Blog Category',
            'organization': 'Organization Name',
        }
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    college = forms.CharField(max_length=100,required=True)
    company = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields =('username','email','password1','password2','college','company')