from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='my_app/static/images', null=True, blank=True)
    placeholder = models.CharField(max_length=100, default=' ', editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'group_id': self.id})
    
class Thread(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=40000, default=" ")

    group = models.ForeignKey(Group, on_delete=models.CASCADE)

