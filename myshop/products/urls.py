from django.urls import path
from . import views # Both imports are needed for the url file.
urlpatterns = [ # matched urls request views. 
    path('', views.index),
    # '' homepage , .index is a function in views, no () needed here
    path('products', views.index, name="home"), # third param name for using on href with django
    path('products/<product>', views.product_cat, name="productcat"), # dynamic url
    # to add more params use /<param01>/<param02>
    path('signup', views.signup, name="signup"), # signup page, tried using products/signup didn't
    # work since it was getting captured by products/<product> so a different url was needed
]
