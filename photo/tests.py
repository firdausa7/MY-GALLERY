from django.test import TestCase

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
        self.new_tag = tags(name="testing")
        self.new_tag.save()


