from django.contrib import admin
from .models import Shirt, Product
# Register your models here.
admin.site.register(Shirt) # add this command to import models you created
admin.site.register(Product)