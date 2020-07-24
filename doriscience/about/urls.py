from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.cv, name='cv'),
    path('hobbies', views.hobbies, name='hobbies'),
    path('pdf', views.generate_pdf, name='about_pdf'),
]