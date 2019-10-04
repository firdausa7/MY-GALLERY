from django.db import models

# Create your models here.

# MODEL FOR LOCATION
####################
class Location(models.Model):
    name = models.CharField(max_length=30)

    '''Method to filter database result'''
    def __str__(self):
        return self.name

# MODEL FOR TAGS
#################
class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()
    def delete_tags(self):
        self.delete()
    def __str__(self):
        return self.name

# MODEL FOR CATEGORY
####################
class Category(models.Model):
    # Attribute Variables of Class Category
    name = models.CharField(max_length=30)

    '''Method to filter database result'''
    def __str__(self):
        return self.name

#MODEL FOR IMAGE
################
class Image(models.Model):
    # Attribute Variables of Class Category
    '''name of image taken '''
    name = models.CharField(max_length=30)
    '''image posted '''
    image = models.ImageField(upload_to='pics/')
    ''' description of image '''
    description = models.CharField(max_length=30)
    ''' the location the picture was taken '''
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null='True', blank=True)
    ''' The category the image is placed in '''
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null='True', blank=True)
