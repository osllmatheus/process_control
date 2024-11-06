from django.urls import path
from . import views

urlpatterns = [
    path('', views.processo_list, name='processo_list'),
    path('<int:pk>/', views.processo_detail, name='processo_detail'),
    path('novo_processo/', views.processo_new, name='processo_new'),
    path('edit/<int:pk>/', views.processo_edit, name='processo_edit'),
    path('delete/<int:pk>/', views.processo_delete, name='processo_delete'),
    path('subprocesso/', views.sub_processo_list, name='subprocesso_list'),
    path('subprocesso/<int:pk>/', views.sub_processo_detail, name='subprocesso_detail'),
    path('novo_subprocesso/', views.sub_processo_new, name='subprocesso_new'),
    path('subprocesso/edit/<int:pk>/', views.sub_processo_edit, name='subprocesso_edit'),
    path('subprocesso/delete/<int:pk>/', views.sub_processo_delete, name='subprocesso_delete'),
]