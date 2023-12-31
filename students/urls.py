from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    
    path('about/', views.about),
    
    path('contact/', views.contact),
    
    path('service/', views.service),
    
    path('thank/', views.thank),
    
    path('saveform/', views.saveEnquiry,name="saveform")
]
