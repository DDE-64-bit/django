from django.urls import path
from . import views

urlpatterns = [
    path("getProducts/<int:pk>", views.ProductList.as_view()),
    path("addProduct", views.AddProduct.as_view()),
]
