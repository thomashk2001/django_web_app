from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import Product
# Create your views here.

def index(request):
  # to return an html, inside the templates folder. By default djang looks in this
  # foloder. We add the folder name of the app in this case products to avoid confusions that
  # it takes another file with the same name on a different web app
  # takes a third parameter that is a dictionary to pass content to the html file
  produdct_numb = "4"
  products = Product.objects.all()
  return render(request, "products/home.html",{
    "name": "tom",
    "product_numb":produdct_numb,
    "products": products,
    })
def product_cat(request, product):
  # the parameter product is basically what comes after the second slash because
  # it was specified that way on the url.py 
  # TODO: Search for multiple parameter pass via url
  accepted_products = ('suit', 'dress', 'shoes', 'shit')
  if product.lower() in accepted_products:
    return HttpResponse(f"Here is a list of our {product}")
  else:
    return HttpResponseNotFound("Object not found")
def signup(request):
  return render(request, "products/signup.html")