from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.CharField(max_length=512)

"""
{
  "name": "Example Product",
  "price": 19.99,
  "description": "This is a sample product."
}
"""