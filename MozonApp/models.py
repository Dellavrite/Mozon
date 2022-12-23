from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

class Сategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    specifications = models.TextField()
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    picture = models.ImageField()
    category = models.ForeignKey(Сategory, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    products_count = models.IntegerField()
    price = models.IntegerField()
    person_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=63)
    
    def __str__(self) -> str:
        return self.product.name

    
