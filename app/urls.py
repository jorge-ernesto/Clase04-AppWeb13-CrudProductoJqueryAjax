from django.urls import path
from app import views

urlpatterns = [  
    path(''                         , views.index         , name="index"),
    path('products/'                , views.product_list  , name='product_list'),
    path('create/'                  , views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
