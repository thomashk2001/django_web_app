from django.contrib import admin
from .models import Shirt, Product
# Register your models here.

class ReadOnlyFields(admin.ModelAdmin):
  readonly_fields = ("slug",)


admin.site.register(Shirt) # add this command to import models you created
admin.site.register(Product, ReadOnlyFields)