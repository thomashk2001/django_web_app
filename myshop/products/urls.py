from django.urls import path
from . import views # Both imports are needed for the url file.
urlpatterns = [ # matched urls request views. 
    path('', views.index),
    # '' homepage , .index is a function in views, no () needed here
    path('products', views.index),
    path('products/<product>', views.product_cat), # dynamic url
    path('signup', views.signup), # signup page, tried using products/signup didnt
    # work since it was getting captured by products/<product> so a different url was needed
]
