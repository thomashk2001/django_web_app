from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
import django.http as dj
# Create your views here.

def index(request):
  # to return an html, inside the templates folder. By default djang looks in this
  # foloder. We add the folder name of the app in this case products to avoid confusions that
  # it takes another file with the same name on a different web app
  # takes a third parameter that is a dictionary to pass content to the html file
  produdct_numb = "4"
  return render(request, "products/home.html",{
    "name": "tom",
    "product_numb":produdct_numb,
    })
def product_cat(request, product):
  accepted_products = ('suit', 'dress', 'shoes', 'shit')
  if product.lower in accepted_products:
    return HttpResponse(f"Here is a list of our {product}")
  else:
    return HttpResponseNotFound("Object not found")