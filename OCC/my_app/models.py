from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='my_app/static/images', height_field='height', width_field='width', null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)

    def __str__ (self):
        return self.name