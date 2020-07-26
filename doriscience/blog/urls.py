from django.urls import path
from . import views

urlpatterns = [
    path('', views.allentries, name='blog'),
    path('<int:entry_id>/', views.entry, name='entry')
]