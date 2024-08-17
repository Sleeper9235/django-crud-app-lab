from django.db import models
from django.urls import reverse

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='my_app/static/images', null=True, blank=True)
    placeholder = models.CharField(max_length=100, default=' ', editable=False)

    
    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'group_id': self.id})