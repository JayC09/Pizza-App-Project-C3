from django.db import models

# Create your models here.
class pizza(models.Model):
    pizza_name = models.CharField(max_length=30)
    pizza_type = models.CharField(max_length=30)
    pizza_size = models.CharField(max_length=100)
    pizza_toppings = models.CharField(max_length=100)