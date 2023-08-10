from django.urls import path
import views  # Both imports are needed for the url file.
urlpatterns = [ # matched urls request views. 
    path('', views.index) 
    # '' homepage , .index is a function in views, no () needed here
]
