from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
        name = models.CharField("Category", max_length=150)
        description = models.TextField()
        
        def __str__(self):
            return self.name


class Post(models.Model):
    author = models.ManyToManyField(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
