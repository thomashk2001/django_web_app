from django.contrib import admin
from .models import Shirt, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  readonly_fields = ("slug",)
  list_display = ("title", "id", "category", "is_bestseller")
  list_filter = ("is_bestseller", )
  search_fields = ("title", "category", "brand")


admin.site.register(Shirt) # add this command to import models you created
admin.site.register(Product, ProductAdmin)