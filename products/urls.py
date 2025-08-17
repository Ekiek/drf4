from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='product_add'),
    path('<int:pk>/edit/', views.edit_product, name='product_edit'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
