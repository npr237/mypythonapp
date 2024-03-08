from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Harry Icecreams Admin"
admin.site.site_title = "Harry icecreams Admin Portal"
admin.site.index_title = "Welcome to Harry icecreams Portal"

urlpatterns = [
 path("", views.index, name='home'),
 path("about", views.about, name='about'),
 path("services", views.services, name='services'),
 path("contact", views.contact, name='contact')
]