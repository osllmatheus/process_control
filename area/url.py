from django.urls import path
from . import views

urlpatterns = [
    path('', views.area_list, name='area_list'),
    path('<int:pk>/', views.area_detail, name='area_detail'),
    path('nova_area/', views.area_new, name='area_new'),
    path('edit/<int:pk>/', views.area_edit, name='area_edit'),
    path('delete/<int:pk>/', views.area_delete, name='area_delete'),
]