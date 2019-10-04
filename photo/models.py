from django.db import models

# Create your models here.

# MODEL FOR LOCATION
class Location(models.Model):
    name = models.CharField(max_length=30)

    '''Method to filter database result'''
    def __str__(self):
        return self.name

# MODEL FOR TAGS
class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
