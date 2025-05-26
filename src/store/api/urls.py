from django.urls import path
from . import views

urlpatterns = [
    path("getProducts", views.getProducts),
    path("getProduct/<int:pk>", views.ProductList.as_view()),
    path("addProducts", views.addProduct),
]
