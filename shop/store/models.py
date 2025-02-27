from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.product.name}"
