from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('times/', views.all_classes, name='all_classes'),
    path('add/', views.add_class, name='add_class'),
    path('edit/<int:class_id>/',
         views.edit_class, name='edit_class'),
]
