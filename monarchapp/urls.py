from django.urls import path
from monarchapp import views
urlpatterns = [
    path("", views.index, name='home'), 
    path("open/", views.openfile, name='openfile'), 
    
]