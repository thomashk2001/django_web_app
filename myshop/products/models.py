from django.db import models

# Create your models here.
class Shirt(models.Model):
  title = models.CharField(max_length= 70)
  price = models.PositiveIntegerField()
  brand = models.CharField(max_length= 50, null= True) # db level
  description = models.TextField(blank=True) # app level
  is_bestseller = models.BooleanField(default=False)
  # in other types of data both must be set. see blank vs null 
# create a an instance of the model as an object and use .save() to save to db
# to get data:
# All: x = Shirt.objects.all()
# One: x = Shirt.objects.get(attribute = value) can only get one if more error occurs
# FIlter: x = Shirt.objects.filter(attribute = value or condition) can get 1 or more
# THIS FUNCTIONS CAN RETURN EMPTY LIST. add .exist() to check if object in db FileExistsError
# Shirt.objects.filter(attribute = value or condition).exists()
# to update get the model in a variable then change attribute then call .save()
# to delete get the model in a variable and then call .delete()
