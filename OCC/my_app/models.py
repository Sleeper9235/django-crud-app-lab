from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.FilePathField(path = "my_app/static/images")

    def __str__ (self):
        return self.name