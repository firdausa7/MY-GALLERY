from django.test import TestCase
from .models import Location, tags, Category, Image

# Create your tests here.

# Test for Location
class LocationTestClass(TestCase):

    #SetUp method  for Location
    def setUp(self):
        self.test_location = Location(name ='Nairobi')
        self.test_location.save()

        #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.test_location, Location))

        # Creating a new tag and saving it
        self.new_tag = tags(name="programming")
        self.new_tag.save()

# Test for Image
class ImageTestClass(TestCase):

    #set up method for Image
    def setUp(self):

        self.category = Category(category_name='Photography')
        self.category.save()

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)



