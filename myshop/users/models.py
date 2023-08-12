from django.db import models

# Create your models here.

class Profile(models.Model):
  full_name: models.CharField(max_length= 100)
  email: models.EmailField(max_length=254)
  birthdate = models.DateField()