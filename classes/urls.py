from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('times', views.all_classes, name='all_classes'),
]
