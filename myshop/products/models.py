from django.db import models

# Create your models here.
class Shirt(models.Model):
  title = models.CharField(max_length= 70)
  price = models.PositiveIntegerField()
  brand = models.CharField(max_length= 50, null= True) # db level
  description = models.TextField(blank=True) # app level
  is_bestseller = models.BooleanField(default=False)
  def __str__(self):
    return f"{self.title}"
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
# to use Find it does not understand <=, >=, we need to use field look ups. PDF.
# Example .filter(price<20) translate to .filter(price__lt=25).
# we use , as AND ex ,filter(x = val, y = val)
# for OR we need to import django.db.models import Q and then
#.filter(Q(x = val) | Q(y = val))
class Product(models.Model):
  title = models.CharField(max_length= 70)
  description = models.TextField()
  category = models.CharField(max_length= 50)
  image = models.ImageField(blank=True, null= True, upload_to='product_img')
  # upload_to specifies where inside the root media directory the image is added.
  brand = models.CharField(max_length= 50)
  price = models.PositiveIntegerField()
  slug = models.SlugField(default=0)
  def __str__(self):
    return f"{self.title}"
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    self.slug = self.id
    super().save(*args, **kwargs)