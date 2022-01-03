from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_memberships, name='memberships'),
    path('add/', views.add_membership, name='add_membership'),
    path('edit/<membership_id>/', views.edit_membership,
         name='edit_membership'),
]
