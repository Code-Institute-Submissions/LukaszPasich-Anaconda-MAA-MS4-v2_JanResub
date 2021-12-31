from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('times/', views.all_classes, name='all_classes'),
    path('edit_classes/<int:class_id>/', views.edit_classes, name='edit_classes'),
]
