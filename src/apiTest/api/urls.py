from django.urls import path
from . import views

urlpatterns = [
    path('getProducts/', views.GetProducts.as_view()),
    path('getProducts/<int:pk>/', views.GetProducts.as_view()),
    path("addProduct/", views.AddProduct.as_view()),
]
