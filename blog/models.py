from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    statuses = [
        ("D","Draft"),
        ("P","Published"),
    ] 
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=1,choices=statuses)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'slug':self.slug})

