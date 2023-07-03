from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('hello',views.helloworld) ,
    path('',views.home_page),
    path('analytics',views.analytics),
    path('<slug:customname>',views.redirect_url)
  

    
    # above hello is ntg but https://localhost/8000/hello
]
